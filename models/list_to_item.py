from main import db
from datetime import datetime

class ListToItem(db.Model):
    __tablename__ = "list_to_items"

    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.ForeignKey('lists.id'), primary_key=True)
    user_to_items_id = db.Column(db.ForeignKey('user_to_items.id'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, list_id, user_to_item_id):
        self.list_id = list_id
        self.user_to_item_id = user_to_item_id