from business_logic import db
from flask_login import UserMixin

class Items(db.Model):
    __tablename__ = "items"
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), nullable=False)
    item_img = db.Column(db.String(200), nullable=False)
    item_price = db.Column(db.Integer, nullable=False)
    cat_id = db.Column(db.String(50), db.ForeignKey('category.foreign_id'), nullable=False)

    def __init__(self,item_id,item_name,item_img,item_price,cat_id):
        self.item_id = item_id
        self.item_name = item_name
        self.item_img = item_img
        self.item_price=item_price
        self.cat_id = cat_id


class Registration(db.Model, UserMixin):
    __tablename__ = "registration"
    Sno = db.Column(db.Integer, primary_key=True,)
    fullname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email= db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    ph_no = db.Column(db.BIGINT, nullable=False)

    def __init__(self, fullname, username, email , password, ph_no):

        self.fullname = fullname
        self.username = username
        self.email= email
        self.password = password
        self.ph_no = ph_no
