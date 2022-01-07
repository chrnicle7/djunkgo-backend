from flask import Blueprint
from flask_restful import Api

from resources import DashboardResource

DASHBOARD_BLUEPRINT = Blueprint("dashboard", __name__)
Api(DASHBOARD_BLUEPRINT).add_resource(
    DashboardResource, "/dashboard"
)