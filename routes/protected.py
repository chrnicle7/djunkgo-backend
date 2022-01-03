from flask import Blueprint
from flask_restful import Api

from resources import CurrentUserResource

PROTECTED_BLUEPRINT = Blueprint("protected", __name__)
Api(PROTECTED_BLUEPRINT).add_resource(
    CurrentUserResource, "/protected/current-user"
)