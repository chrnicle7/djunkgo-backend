"""
    Libraries
"""
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from main import db
from config import APP_URL, APP_PORT

from helper import GetCurrentUser, RandomStringHelper
from models import UserToItem, Mitra, MitraToItem, Item, List, ListToItem, Transaksi, TransaksiToItem, transaksi, transaksi_to_item, user_to_item

from config import APP_URL, APP_PORT
"""
    Resource
"""
parser = reqparse.RequestParser()
parser.add_argument("mitra_id", type=int, required=True, help="Mitra harus diisi")

class PilihMitraResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        search_param = request.args.get('search')

        user_now = GetCurrentUser().get_current_user()
        list_found = List.query.filter_by(user_id=user_now["id"]).first()
        q_list_item = ListToItem.query.filter_by(list_id=list_found.id).all()
        user_item_id = tuple(q.user_to_items_id for q in q_list_item)
        user_to_items_found = UserToItem.query.filter(UserToItem.id.in_(user_item_id)).all()
        item_id = [q.item_id for q in user_to_items_found]

        if search_param is not None:
            q_mitra_item = Mitra.query.filter(Mitra.nama.match(
                "%" + search_param + "%")).join(MitraToItem).all()
        else:
            q_mitra_item = Mitra.query.all()
        matched_mitras = []

        for q_mitra in q_mitra_item:
            mitra_item_arr = []
            if len(q_mitra.mitra_to_items) > 0:
                for q_items in q_mitra.mitra_to_items:
                    mitra_item_arr.append(q_items.item_id)
                if set(item_id).issubset(set(mitra_item_arr)):
                    matched_mitra = Mitra.query.filter_by(
                        id=q_items.mitra_id).first()
                    matched_mitras.append(matched_mitra.json())

        results = []
        for matched_mitra in matched_mitras:
            result = {
                "id_mitra": matched_mitra["id"],
                "nama_mitra": matched_mitra["nama"],
                "alamat_mitra": matched_mitra["alamat"],
                "rating_mitra": matched_mitra["rating"],
                "path_foto_mitra": matched_mitra["path_foto"],
                "url_mitra": ""
            }
            results.append(result)

        return {"data": results}, 200


class DetailMitraResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, mitra_id):
        results = {}
        mitra_found = Mitra.query.filter_by(id=mitra_id).first()

        results["mitra"] = {
            "nama_mitra": mitra_found.nama,
            "alamat_mitra": mitra_found.alamat,
            "rating_mitra": str(mitra_found.rating),
            "path_foto_mitra": mitra_found.path_foto,
        }
        results["items"] = []

        user_now = GetCurrentUser().get_current_user()
        list_found = List.query.filter_by(user_id=user_now["id"]).first()
        list_to_items = ListToItem.query.filter_by(list_id=list_found.id).all()

        harga_total = 0
        url = APP_URL + ":" + APP_PORT + "/"
        for list_to_item in list_to_items:
            found_user_to_item = UserToItem.query.filter_by(id=list_to_item.user_to_items_id).first()
            found_mitra_item = MitraToItem.query.filter(MitraToItem.mitra_id == mitra_id, MitraToItem.item_id==found_user_to_item.item_id).first()

            if found_mitra_item is None:
                return {"message": "Terdapat kesalahan"}, 500
            found_item = Item.query.filter_by(id=found_user_to_item.item_id).first()
            harga_per_item = found_mitra_item.harga_beli_satuan * found_user_to_item.jumlah
            harga_total += harga_per_item
            res_item = {
                "nama": found_item.nama,
                "harga_x_quantity": "Rp. " + str(found_mitra_item.harga_beli_satuan) + " x " + str(found_user_to_item.jumlah) + " pcs",
                "harga_per_item": harga_per_item,
                "path_foto_item": url + found_user_to_item.path_foto,
            }
            results["items"].append(res_item)

        results["total_harga"] = harga_total
        results["mitra_id"] = mitra_id
            
        return {"data": results}, 200


class KonfirmasiResource(Resource):
        method_decorators = [jwt_required()]

        def post(self):
            args = parser.parse_args()
            user_now = GetCurrentUser().get_current_user()

            list_found = List.query.filter_by(user_id=user_now["id"]).first()
            item_found = list_found.list_to_items
            mitra_found = Mitra.query.filter_by(id=args["mitra_id"]).first()

            if mitra_found is None:
                return {"message": "Mitra tidak ditemukan"}, 404

            harga_total = 0
            user_items_id = []
            for item in item_found:
                found_user_to_item = UserToItem.query.filter_by(id=item.user_to_items_id).first()
                if found_user_to_item.jumlah <= 0:
                    return {"message": "Isi jumlah item terlabih dahulu"}, 500

                found_mitra_item = MitraToItem.query.filter(MitraToItem.mitra_id == mitra_found.id, MitraToItem.item_id==found_user_to_item.item_id).first()
                if found_mitra_item is None:
                    return {"message": "Terdapat kesalahan"}, 500
                harga_satuan_item = found_mitra_item.harga_beli_satuan
                harga_per_item = found_mitra_item.harga_beli_satuan * found_user_to_item.jumlah
                harga_total += harga_per_item

                found_user_to_item.harga_jual_satuan = harga_satuan_item
                found_user_to_item.harga_jual_total = harga_per_item
                found_user_to_item.save_to_db()

                user_items_id.append(found_user_to_item.id)

            transaksi_id = RandomStringHelper.generate_random_str()
            new_transaksi = Transaksi(
                id=transaksi_id,
                user_id=user_now["id"],
                mitra_id = mitra_found.id,
                total_harga_transaksi=harga_total,
            )
            new_transaksi.save_to_db() 
            db.session.refresh(new_transaksi)         

            for item_id in user_items_id:
                new_transaksi_to_item = TransaksiToItem(
                    transaksi_id=new_transaksi.id,
                    user_to_items_id=item_id
                )
                new_transaksi_to_item.save_to_db()

            try:
                ListToItem.query.filter_by(list_id=list_found.id).delete()
            except Exception as e:
                return {"message": "terdapat kesalahan"}, 201
    
            return {"message": "List berhasil dikonfirmasi"}, 201

