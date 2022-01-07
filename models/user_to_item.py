from main import db
from datetime import datetime

class UserToItem(db.Model):
    __tablename__ = "user_to_items"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.ForeignKey("users.id"), primary_key=True)
    item_id = db.Column(db.ForeignKey("items.id"), primary_key=True)
    percentage = db.Column(db.Float)
    jumlah = db.Column(db.Integer)
    is_terjual = db.Column(db.Boolean, default=False)
    harga_jual_satuan = db.Column(db.Integer)
    harga_jual_total = db.Column(db.Integer)
    path_foto = db.Column(db.String(200))
    filename = db.Column(db.String(200))
    mimetype = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    list_to_items = db.relationship("ListToItem", backref="list_to_items", lazy=True)
    transaksi_to_items = db.relationship("TransaksiToItem", backref="transaksi_to_items", lazy=True)

    def json(self):
        return {"user_id": self.user_id, "item_id": self.item_id}

    def __init__(self, user_id, item_id, path_foto, percentage, filename, mimetype):
        self.user_id = user_id
        self.item_id = item_id
        self.percentage = percentage
        self.path_foto = path_foto
        self.filename = filename
        self.mimetype = mimetype