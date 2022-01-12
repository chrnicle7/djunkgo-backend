from flask import Blueprint
from flask_restful import Api

from resources import ItemSayaResource, ItemSayaDetailResource

ITEM_SAYA_BLUEPRINT = Blueprint("item_saya", __name__)
Api(ITEM_SAYA_BLUEPRINT).add_resource(
    ItemSayaResource, "/item-saya"
)

Api(ITEM_SAYA_BLUEPRINT).add_resource(
    ItemSayaDetailResource, "/item-saya/<int:id>"
)