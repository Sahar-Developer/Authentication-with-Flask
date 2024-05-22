from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    # when we do the foreign key we use lower case letters(not User but user)
    # when we are using "one to many" datas like a heirarchical database we use foreign key in order to make the relation between parent and children
    user_id = db.Column(db.Integer , db.ForeignKey('user.id'))
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer , primary_key = True)
    email = db.Column(db.String(150), unique = True)
    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    # when we do the relationship we use the class name as it is (with capital letters(not note but Note))
    notes = db.relationship('Note')


