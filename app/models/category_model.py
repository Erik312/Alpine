from app.models.db import db
from app.models.post_model import Post


class Category(db.Model):
    """ Forum topic Scheme """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    url_s = db.Column(db.String, nullable=False, unique=True)
    posts = db.relationship('Post', backref="category" ,lazy=True)