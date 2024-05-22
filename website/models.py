from . import db
from flask import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer , primary_key = True)
    email = db.Column(db.String(150), unique = True)
    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))


