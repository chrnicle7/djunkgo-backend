from main import db
from datetime import datetime

class Transaksi(db.Model):
    __tablename__ = "transaksis"

    id = db.Column(db.String(32), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    mitra_id = db.Column(db.Integer, db.ForeignKey("mitras.id"), primary_key=True)
    total_harga_transaksi = db.Column(db.Integer)
    status_id = db.Column(db.Integer, db.ForeignKey("status_transaksi.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)