
from flask import Blueprint,render_template


index_bp = Blueprint('index', __name__, url_prefix="/")
@index_bp.route('/')
def index():
    ''' Index route'''
    try:
        return render_template('index.html')
    except Exception as e:
        return("404 Error couldnt find page")