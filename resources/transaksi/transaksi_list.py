"""
    Libraries
"""
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from main import db
from config import APP_URL, APP_PORT
from helper import GetCurrentUser
from models import Transaksi, Mitra, StatusTransaksi, UserToItem, Item

from config import APP_URL, APP_PORT
"""
    Resource
"""

class TransaksiListResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        status_param = request.args.get('status')
        user_now =  GetCurrentUser().get_current_user()
        results = []

        if status_param is not None:
            transaksis_found = Transaksi.query.filter(Transaksi.user_id==user_now["id"], Transaksi.status_id==status_param).all()
        else:
            transaksis_found = Transaksi.query.filter_by(user_id=user_now["id"]).all()

        for transaksi in transaksis_found:
            found_mitra = Mitra.query.filter_by(id=transaksi.mitra_id).first()
            found_status = StatusTransaksi.query.filter_by(id=transaksi.status_id).first()
            result = {
                "nama_mitra": found_mitra.nama,
                "path_foto_mitra": found_mitra.path_foto,
                "total_harga_transaksi": transaksi.total_harga_transaksi,
                "status_transaksi": found_status.nama,
                "transaksi_url": request.base_url + "/" + transaksi.id
            }
            results.append(result)

        return {"data": results}, 200


class TransaksiDetailResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, id):
        transaksi_found = Transaksi.query.filter_by(id=id).first()
        results = {}
        if transaksi_found is None:
            return {"message": "Transaksi tidak ditemukan"}, 400

        found_mitra = Mitra.query.filter_by(id=transaksi_found.mitra_id).first()
        results["mitra"] = {
            "nama_mitra": found_mitra.nama,
            "alamat_mitra": found_mitra.alamat,
            "rating_mitra": str(found_mitra.rating),
            "path_foto_mitra": found_mitra.path_foto,
        }
        harga_total = 0
        url = APP_URL + ":" + APP_PORT + "/"
        
        results["items"] = []
        for item in transaksi_found.transaksis_to_items:
            found_user_item = UserToItem.query.filter_by(id=item.user_to_items_id).first()
            found_item = Item.query.filter_by(id=found_user_item.item_id).first()

            harga_total += found_user_item.harga_jual_total
            item_result = {
                "nama_item": found_item.nama,
                "harga_x_quantity": "Rp. " + str(found_user_item.harga_jual_satuan) + " " + str(found_user_item.jumlah) + " pcs",
                "harga_per_item": found_user_item.harga_jual_total,
                "path_foto": url + found_user_item.path_foto,
            }
            results["items"].append(item_result)

        found_status = StatusTransaksi.query.filter_by(id=transaksi_found.status_id).first()
        results["status"] = found_status.nama

        return {"data": results}