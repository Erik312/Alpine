from datetime import datetime
from app.models.db import db
from app.models.comments_model import Comment



class Post(db.Model):
    ''' Posts Scheme '''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    time_of_creation = db.Column(db.DateTime, default=datetime.utcnow)
    meat_pot = db.Column(db.String, nullable=False)
    username = db.Column(db.String, db.ForeignKey("user.username"))
    comments = db.relationship('Comment', backref="post", lazy=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))




