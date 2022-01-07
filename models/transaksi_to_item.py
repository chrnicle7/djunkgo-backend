from main import db
from datetime import datetime

class TransaksiToItem(db.Model):
    __tablename__ = "transaksi_to_items"

    id = db.Column(db.Integer, primary_key=True)
    transaksi_id = db.Column(db.ForeignKey('transaksis.id'), primary_key=True)
    user_to_item_id = db.Column(db.ForeignKey('user_to_items.id'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, transkasi_id, user_to_item_id):
        self.transaksi_id = transkasi_id
        self.user_to_item_id = user_to_item_id