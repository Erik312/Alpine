from datetime import datetime
from app.models.db import db



class Comment(db.Model):
    ''' Comment reply scheme '''
    id = db.Column(db.Integer, primary_key=True)
    time_of_creation = db.Column(db.DateTime, default=datetime.utcnow)
    meat_pot = db.Column(db.String, nullable=False)
    username = db.Column(db.String, db.ForeignKey("user.username"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
