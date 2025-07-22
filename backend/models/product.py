from models.db import db


class Products(db.Model):
    __tablename__ = 'Products'
    
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String)
    description = db.Column(db.Text , nullable = False)
    price = db.column(db.Numeric(10 , 2) , nullable = False)
    category = db.Column(db.Sting , nullable = False)
    image_url = db.Column(db.Text , nullable = False)
    stock_qty = db.Column(db.Integer , nullable = False)
     
    