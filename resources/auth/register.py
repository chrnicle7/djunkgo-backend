"""
    Libraries
"""
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

from models import User
from helper import PasswordHelper, RandomStringHelper

"""
    Parser 
"""
parser = reqparse.RequestParser()
parser.add_argument("nama", type=str, required=True, help="nama harus diisi")
parser.add_argument("email", type=str, required=True, help="email harus diisi")
parser.add_argument("password", type=str, required=True, help="password harus diisi")

"""
    Resource
"""
class RegisterResource(Resource):

    def post(self):
        args = parser.parse_args()
        user_found = User.find_by_email(User, args["email"]) 

        if user_found is not None:
            return {"message": "Email telah digunakan"}, 200

        string_id = RandomStringHelper.generate_random_str()
        hashed_password = PasswordHelper.hash_password(args["password"])
        user = User(
            id=string_id,
            nama=args["nama"],
            email=args["email"],
            password=hashed_password,
            role_id=2
        )
        try:
            user.save_to_db()
        except Exception as e:
            print(e)
            return {"message": "Terjadi kesalahan ketika mendaftarkan pengguna"}, 500

        return {"message": "Pengguna berhasil terdaftar"}, 201
