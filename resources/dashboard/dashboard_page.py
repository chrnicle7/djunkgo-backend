"""
    Libraries
"""
from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_identity, jwt_required

from main import db

from helper import GetCurrentUser
from models import User, UserToItem, Item

"""
    Resource
"""
class DashboardResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        user_now =  GetCurrentUser().get_current_user()
        q_all = UserToItem.query.filter_by(user_id=user_now["id"]).count()
        q_anorganik = UserToItem.query.filter_by(user_id=user_now["id"]). \
                join(Item).filter_by(is_anorganik=True). \
                count()
        q_organik = UserToItem.query.filter_by(user_id=user_now["id"]). \
                join(Item).filter_by(is_anorganik=False). \
                count()
        q_terjual = UserToItem.query.filter(UserToItem.user_id==user_now["id"], UserToItem.is_terjual==True). \
                count()
        
        return {
            "total_item": q_all,
            "organik": q_organik,
            "anorganik": q_anorganik,
            "terjual": q_terjual
        }