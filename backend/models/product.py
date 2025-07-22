from backend.models.db import db


class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String)
    description = db.Column(db.Text , nullable = False)
    price = db.Column(db.Numeric(10 , 2) , nullable = False)
    category = db.Column(db.String , nullable = False)
    image_url = db.Column(db.Text , nullable = False)
    stock_qty = db.Column(db.Integer , nullable = False)
     
    