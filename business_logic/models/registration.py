from flask_login import UserMixin

from business_logic import db


class Registration(db.Model, UserMixin):
    __tablename__ = "registration"
    Sno = db.Column(db.Integer, primary_key=True, )
    fullname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    ph_no = db.Column(db.BIGINT, nullable=False)

    def __init__(self, fullname, username, email, password, ph_no):
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password
        self.ph_no = ph_no

    def __repr__(self):
        print(
            f"Fullname: {self.fullname} \nUsername: {self.username} \nEmail: {self.email} \n Password: {'*' * len(self.password)} \nPhone Number: {self.ph_no}")
