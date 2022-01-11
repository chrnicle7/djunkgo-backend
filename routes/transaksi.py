
from flask import Blueprint
from flask_restful import Api

from resources import TransaksiListResource, TransaksiDetailResource

TRANSAKSI_BLUEPRINT = Blueprint("transaksi", __name__)
Api(TRANSAKSI_BLUEPRINT).add_resource(
    TransaksiListResource, "/transaksi"
)

Api(TRANSAKSI_BLUEPRINT).add_resource(
    TransaksiDetailResource, "/transaksi/<id>"
)

