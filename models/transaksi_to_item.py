from main import db
from datetime import datetime

class TransaksiToItem(db.Model):
    __tablename__ = "transaksis_to_item"

    id = db.Column(db.Integer, primary_key=True)
    transaksi_id = db.Column(db.ForeignKey('transaksis.id'), primary_key=True)
    user_to_items_id = db.Column(db.ForeignKey('user_to_items.id'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, transaksi_id, user_to_items_id):
        self.transaksi_id = transaksi_id
        self.user_to_items_id = user_to_items_id

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
