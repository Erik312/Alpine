from app.models.db import db


class User(db.Model):
    ''' Forum user scheme '''
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique=True,nullable=False)
    email = db.Column(db.String,unique=True,nullable=False)
    password = db.Column(db.String,nullable=False)
    posts_count = db.Column(db.Integer,default=0)
    comments_count = db.Column(db.Integer,default=0)
    is_admin = db.Column(db.Boolean, default=False)