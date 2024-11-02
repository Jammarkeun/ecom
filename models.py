from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String, nullable=False)  # Correct


class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    joined_date = db.Column(db.DateTime, default=func.now())