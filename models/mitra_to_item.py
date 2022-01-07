from main import db
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MitraToItem(Base):
    __tablename__ = "mitra_to_item"

    id = db.Column(db.Integer, primary_key=True)
    mitra_id = db.Column(db.ForeignKey('mitras.id'), primary_key=True)
    item_id = db.Column(db.ForeignKey('items.id'), primary_key=True)
    harga_beli_satuan = db.Column(db.Integer)
    min_beli = db.Column(db.Integer)
    max_beli = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)