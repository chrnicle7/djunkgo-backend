from main import db
from datetime import datetime

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(200))
    is_anorganik = db.Column(db.Boolean, default=False)
    is_dapat_dijual = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_to_items = db.relationship("UserToItem", backref="user_to_items_item", lazy=True)
