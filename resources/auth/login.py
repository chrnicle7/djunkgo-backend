"""
    Libraries
"""
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

from models import User
from helper import PasswordHelper

"""
    Parser 
"""
parser = reqparse.RequestParser()
parser.add_argument("email", type=str, required=True, help="Email harus diisi")
parser.add_argument("password", type=str, required=True, help="Pasword harus diisi")

"""
    Resource
"""
class LoginResource(Resource):
    def post(self):
        args = parser.parse_args()
        user_found = User.find_by_email(User, args["email"])

        if user_found is None:
            return {"message": "Pengguna tidak ditemukan"}, 401

        if not PasswordHelper.check_password_hash(args["password"], user_found.password):
            return {"message": "Password salah"}, 401

        access_token = create_access_token(identity=user_found.email)
        return {"token": access_token}