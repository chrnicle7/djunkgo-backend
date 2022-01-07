from main import db
from datetime import datetime

class StatusTransaksi(db.Model):
    __tablename__ = "status_transaksi"

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)