"""
    Libraries
"""
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from main import db
from config import APP_URL, APP_PORT

from helper import GetCurrentUser
from models import UserToItem, Mitra, MitraToItem, Item, List, ListToItem
from config import APP_URL, APP_PORT
"""
    Resource
"""

class DaftarMitraResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        search_param = request.args.get('search')

        if search_param is not None:
            q_mitras = Mitra.query.filter(Mitra.nama.match(
                "%" + search_param + "%")).join(MitraToItem).all()
        else:
            q_mitras = Mitra.query.all()

        results = []
        for mitra in q_mitras:
            result = {
                "id_mitra": mitra.id,
                "nama_mitra": mitra.nama,
                "alamat_mitra": mitra.alamat,
                "rating_mitra": str(mitra.rating),
                "path_foto_mitra": mitra.path_foto,
                "url_mitra": request.base_url + "/" + str(mitra.id)
            }
            results.append(result)

        return {"data": results}, 200


class DetailMitraResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, id):
        results = {}
        mitra_found = Mitra.query.filter_by(id=id).first()
        if mitra_found is None:
            return {"message": "Mitra tidak ditemukan"}, 404

        items_found = mitra_found.mitra_to_items
        if items_found is None:
            return {"message": "Item tidak ditemukan"}, 404

        results["mitra"] = {
            "nama_mitra": mitra_found.nama,
            "alamat_mitra": mitra_found.alamat,
            "rating_mitra": str(mitra_found.rating),
            "path_foto_mitra": mitra_found.path_foto,
        }
        results["items"] = []

        url = APP_URL + ":" + APP_PORT + "/"
        for item in items_found:
            item_found = Item.query.filter_by(id=item.item_id).first()
            res_item = {
                "nama": item_found.nama,
                "harga_satuan": "Rp." + str(item.harga_beli_satuan) + "/pcs",
            }
            results["items"].append(res_item)
            
        return {"data": results}, 200
