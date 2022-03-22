from business_logic import db


class Order(db.models):
    __tablename__ = "cart"
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('registration.Sno'))
    order_detail = db.Column(db.Text(45), nullable=False)
    total_amount = db.Column(db.Integer(50), nullable=False)

    def __init__(self, order_id,user_id,order_detals,total_amount):
        self.order_id = order_id
        self.user_id = user_id
        self.order_detals=order_detals
        self.total_amount=total_amount
