"""
    Libraries
"""
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from models import User, user

"""
    Helper
"""
class GetCurrentUser:

    @staticmethod
    def get_current_user():
        email = get_jwt_identity()
        user_found = User.find_by_email(User, email)

        return user_found.json()