from smit import db



class Items(db.Model):
    __tablename__ = "items"
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), nullable=False)
    item_img = db.Column(db.String(200), nullable=False)
    item_price = db.Column(db.Integer, nullable=False)
    cat_id = db.Column(db.String(50), db.ForeignKey('category.foreign_id'), nullable=False)

    def __init__(self,item_name,item_img,item_price):
        self.item_name = item_name
        self.item_img = item_img
        self.item_price=item_price

    def __repr__(self):
        return f"items('{self.item_name}', '{self.item_img}', '{self.item_price}')"
