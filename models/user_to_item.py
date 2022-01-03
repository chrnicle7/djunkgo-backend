from main import db
from datetime import datetime

class UserToItem(db.Base):
    __tablename__ = "user_to_item"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'), primary_key=True)
    item_id = db.Column(db.ForeignKey('items.id'), primary_key=True)
    jumlah = db.Column(db.Integer)
    is_terjual = db.Column(db.Boolean, default=False)
    harga_jual_satuan = db.Column(db.Integer)
    harga_jual_total = db.Column(db.Integer)
    path_foto = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)