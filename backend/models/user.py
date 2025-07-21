from models.db import db
from datetime import datetime
from sqlalchemy import Enum
import enum

class Roletype(enum.Enum):
    admin = "admin"
    customer = "customer"

class Users(db.Model):
    __tablename__ = 'Users'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String , nullable = False , unique = True)
    email = db.Column(db.String , unique = True , nullable = False)
    role = db.Column(Enum(Roletype), nullable = False)
    password_hash = db.Column(db.Text , nullable = False)
    created_at = db.Column(db.DateTime , default=datetime.utcnow)