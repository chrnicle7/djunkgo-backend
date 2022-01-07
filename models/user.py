from main import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(200), primary_key=True)
    nama = db.Column(db.String(200))
    email = db.Column(db.String(50))
    password = db.Column(db.String(200))
    no_hp = db.Column(db.String(20))
    alamat = db.Column(db.Text)
    path_foto = db.Column(db.String(200))
    filename = db.Column(db.String(200))
    mimetype = db.Column(db.String(200))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), primary_key=True)
    email_verification_sent_at = db.Column(db.DateTime, default=datetime.utcnow)
    email_verification_verified_at = db.Column(db.DateTime, default=datetime.utcnow)
    forgot_password_token = db.Column(db.String(500))
    password_sent_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_to_items = db.relationship("UserToItem", backref="user_to_items_user", lazy=True)

    def __init__(self, id, nama, email, password, role_id):
        self.id = id
        self.nama = nama
        self.email = email
        self.password = password
        self.role_id = role_id

    def __getitem__(self, arg):
        return arg

    def __setitem__(self, arg):
        return arg

    def json(self):
        return {"id": self.id, "nama": self.nama, "email": self.email, "role_id": self.role_id}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get_or_404(id)

    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def find_by_role(cls, role_id):
        return cls.query.filter_by(role_id=role_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()