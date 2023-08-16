from flask import Blueprint,session,redirect,render_template,request
from app.models.db import db



logout_bp = Blueprint('logout',__name__,url_prefix='/logout')


@logout_bp.route('/', methods=['GET','POST'])
def logout():
    ''' logout '''
    try:
        session.clear()
        return redirect('/')
    except Exception as e:
        return ('<h1> 500:An error has occured</h1>')