from main import db
from datetime import datetime

from models import user

class Transaksi(db.Model):
    __tablename__ = "transaksis"

    id = db.Column(db.String(32), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    mitra_id = db.Column(db.Integer, db.ForeignKey("mitras.id"), primary_key=True)
    total_harga_transaksi = db.Column(db.Integer)
    status_id = db.Column(db.Integer, db.ForeignKey("status_transaksi.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    transaksis_to_items = db.relationship("TransaksiToItem", backref="transaksis_to_item", lazy=True)

    def __init__(self, id, user_id, mitra_id, total_harga_transaksi):
        self.id = id
        self.user_id = user_id
        self.mitra_id = mitra_id
        self.total_harga_transaksi = total_harga_transaksi
        self.status_id = 1

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()