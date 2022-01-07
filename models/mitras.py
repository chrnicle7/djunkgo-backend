from main import db
from datetime import datetime

class Mitra(db.Model):
    __tablename__ = "mitras"

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(200))
    rating = db.Column(db.Numeric(1, 1))
    alamat = db.Column(db.Text)
    path_foto = db.Column(db.String(200))
    filename = db.Column(db.String(200))
    mimetype = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)