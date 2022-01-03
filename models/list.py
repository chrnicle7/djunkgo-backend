from main import db
from datetime import datetime

class List(db.Model):
    __tablename__ = "lists"

    id = db.Column(db.String(32), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    mitra_id = db.Column(db.Integer, db.ForeignKey("mitras.id"), primary_key=True)
    harga_jual_total = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)