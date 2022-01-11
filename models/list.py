from main import db
from datetime import datetime

class List(db.Model):
    __tablename__ = "lists"

    id = db.Column(db.String(32), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    list_to_items = db.relationship("ListToItem", backref="list_to_items_list", lazy=True)

    def __init__(self, id, user_id):
        self.id = id
        self.user_id = user_id

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()