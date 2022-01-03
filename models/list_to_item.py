from main import db
from datetime import datetime

class ListsToItem(db.Base):
    __tablename__ = "mitra_to_item"

    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.ForeignKey('lists.id'), primary_key=True)
    user_to_item_id = db.Column(db.ForeignKey('user_to_item.id'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)