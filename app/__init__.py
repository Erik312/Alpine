import os
from flask import Flask


def init_app():
    ''' Main Application Factory '''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///forum3.db" #insert you database name
    app.secret_key = "*your&super\secret/key" #*important* Change to a secure key of your own choosing. Use an env file/variable. 
    from .models.db import db
    from .utilities.create_forum_category import CatCreate

    db.init_app(app)

    with app.app_context():
        from .routes.index_route import index_bp
        from .routes.login_route import login_bp
        from .routes.signup_route import signup_bp
        from .routes.home_route import home_bp
        from .routes.logout_route import logout_bp
        from .routes.forum_main_route import forum_main_bp
        from .routes.post_route import post_bp
        from .routes.comment_route import comment_bp

        app.register_blueprint(index_bp)
        app.register_blueprint(login_bp)
        app.register_blueprint(signup_bp)
        app.register_blueprint(home_bp)
        app.register_blueprint(logout_bp)
        app.register_blueprint(forum_main_bp)
        app.register_blueprint(post_bp)
        app.register_blueprint(comment_bp)

        db.create_all()#creates db Models
        CatCreate()#creates forum topics



    return app