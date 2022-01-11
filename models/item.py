from main import db
from datetime import datetime

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(200))
    is_anorganik = db.Column(db.Boolean, default=False)
    is_dapat_dijual = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_to_items = db.relationship("UserToItem", backref="user_to_items_item", lazy=True)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

