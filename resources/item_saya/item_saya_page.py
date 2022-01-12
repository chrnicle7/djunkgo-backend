"""
    Libraries
"""
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_identity, jwt_required

from main import db
from config import APP_URL, APP_PORT

from helper import GetCurrentUser
from models import List, UserToItem, Item
from models import user
from models.list_to_item import ListToItem
from models.user import User

"""
    Parser 
"""
parser = reqparse.RequestParser()
parser.add_argument("jumlah", type=int, required=True, help="Jumlah harus diisi")


"""
    Resource
"""
class ItemSayaResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        user_now =  GetCurrentUser().get_current_user()
        q_all = UserToItem.query.filter_by(user_id=user_now["id"]).all()
        results = []
        
        if len(q_all) > 0:
            for q in q_all:
                item_found = Item.find_by_id(q.item_id)

                if item_found is not None:
                    result = {
                        "id": q.id,
                        "nama_item": item_found.nama,
                        "jumlah": str(q.jumlah) + " pcs",
                        "jenis": "anorganik" if item_found.is_anorganik else "organik",
                        "url_delete": request.base_url + "/" + str(q.id)
                    }
                    results.append(result)

        return {"data": results}, 200


class ItemSayaDetailResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, id):
        try:
            q = UserToItem.find_by_id(id)
            item = Item.query.filter_by(id=q.item_id).first()
        except Exception as e:
            return {
                "message": e
            }, 404

        q_url_img = APP_URL + ":" + APP_PORT

        return {
            "data" : 
                {
                    "id": q.id,
                    "nama": item.nama,
                    "jumlah": q.jumlah,
                    "jenis": "anorganik" if item.is_anorganik else "organik",
                    "url_delete": request.base_url,
                    "url_foto": q_url_img + "/" + q.path_foto,
                    "is_anorganik": item.is_anorganik,
                    "is_dapat_dijual": item.is_dapat_dijual,
                }
            }