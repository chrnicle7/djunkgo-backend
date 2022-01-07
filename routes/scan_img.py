from flask import Blueprint
from flask_restful import Api

from resources import ScanImageResource

SCAN_IMG_BLUEPRINT = Blueprint("scan-img", __name__)
Api(SCAN_IMG_BLUEPRINT).add_resource(
    ScanImageResource, "/scan-img"
)
