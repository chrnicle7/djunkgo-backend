from flask import Blueprint
from flask_restful import Api

from resources import ListSayaResource, ListSayaDetailResource, PilihMitraResource, DetailMitraResource
from resources.list_saya.pilih_mitra_page import KonfirmasiResource

LIST_SAYA_BLUEPRINT = Blueprint("list_saya", __name__)
Api(LIST_SAYA_BLUEPRINT).add_resource(
    ListSayaResource, "/list-saya"
)

Api(LIST_SAYA_BLUEPRINT).add_resource(
    ListSayaDetailResource, "/list-saya/<int:id>"
)

Api(LIST_SAYA_BLUEPRINT).add_resource(
    PilihMitraResource, "/pilih-mitra"
)

Api(LIST_SAYA_BLUEPRINT).add_resource(
    DetailMitraResource, "/pilih-mitra/<int:mitra_id>"
)

Api(LIST_SAYA_BLUEPRINT).add_resource(
    KonfirmasiResource, "/konfirmasi-list"
)