from business_logic import db


class Cart(db.Model):
    __tablename__ = "cart"
    order_id = db.Column(db.Integer, primary_key=True)
    order_detail = db.Column(db.String(5000), nullable=False)
    total_amount = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('registration.Sno'))

    def __init__(self, order_detail,total_amount):
        self.order_detail=order_detail
        self.total_amount=total_amount
