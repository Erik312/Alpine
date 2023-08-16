
from flask import Blueprint,render_template,request,redirect,session
from app.models.db import db
from app.models.user_model import User

login_bp=Blueprint('login', __name__, url_prefix="/login")

@login_bp.route('/', methods=['GET','POST'])
def login():
    ''' Login '''
    if 'username' in session:
        return redirect('/home')
    else:

        if request.method == 'POST':
            if request.form['email'] == "" or request.form['password'] == "":
                print("fields cannot be empty")
                return redirect('/login')
            else:
                user_email = request.form['email']
                user_password  = request.form['password']
                user_query = db.session.execute(db.select(User).filter_by(email=user_email)).scalar()
                if user_query == None:
                    print('An error occured')
                    return redirect('/login')
                else:
                    if user_password != user_query.password:
                        print("An error occcured")
                        return redirect('/login')
                    else:
                        session['username'] = user_query.username
                        print("login success")
                        return redirect('/home')
        else:
            try:
                return render_template('login.html')
            except Exception as e:
                return('404 couldnt find page')