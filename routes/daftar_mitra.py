from flask import Blueprint
from flask_restful import Api

from resources import DaftarMitraResource, DetailMitraResource

DAFTAR_MITRA_BLUEPRINT = Blueprint("daftar_mitra", __name__)
Api(DAFTAR_MITRA_BLUEPRINT).add_resource(
    DaftarMitraResource, "/daftar-mitra"
)
Api(DAFTAR_MITRA_BLUEPRINT).add_resource(
    DetailMitraResource, "/daftar-mitra/<int:id>"
)