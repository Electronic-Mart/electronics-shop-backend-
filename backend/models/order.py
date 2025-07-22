from models.db import db
from datetime import datetime


class Orders:
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer , primary_key = True)
    user_id = db.column(db.String , db.ForeignKey('users.id' , ondelete = 'CASCADE'), nullable = False)
    total = db.Column(db.Numeric(10 , 2), nullable = False)
    status = db.Column(db.String)
    created_at = db.Column(db.DateTime , default = datetime.utcnow)
    
    user = db.relationship('User' , back_populates = 'orders')
    