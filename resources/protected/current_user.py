"""
    Libraries
"""
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from helper import GetCurrentUser

"""
    Resource
"""
class CurrentUserResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        return GetCurrentUser().get_current_user()