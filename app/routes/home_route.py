from flask import Blueprint,render_template,session,redirect,request


home_bp = Blueprint('home', __name__, url_prefix="/home")


@home_bp.route('/')
def home():
    ''' Home page route '''
    if 'username' not in session:
        return redirect('/login')
    else:
        try:
            return render_template('home.html')
        except Exception as e:
            return("<h1>404 Error couldnt find page</h1>")