from flask import Blueprint,render_template,request,redirect,session
from app.models.db import db
from app.models.user_model import User




signup_bp = Blueprint("signup", __name__, url_prefix="/signup")

@signup_bp.route('/', methods=['GET','POST'])
def signup():
    ''' User sign up '''
    if 'username' in session:
        return redirect('/home')
    else:
        if request.method == 'POST':
            form_data = request.form
            if request.form['username'] == "" or request.form['email'] == "" or request.form['password'] == "":
                print("fields cannot be empty")
                return redirect('/signup')
            else:
                try:
                    new_user = User(username=request.form['username'],email=request.form['email'],password=request.form['password'])
                    db.session.add(new_user)
                    db.session.commit()
                    return redirect('/login')
                except Exception as e:
                    return(e,"Error creating user")
        else:
            try:
                return render_template("signup.html")
            except Exception as e:
                return('<h1> 404 Error couldnt reach page </h1>')