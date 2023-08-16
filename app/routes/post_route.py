from flask import Blueprint,request,redirect,session,render_template,url_for
from app.models.db import db
from app.models.category_model import Category
from app.models.post_model import Post
from app.models.user_model import User
from app.models.comments_model import Comment



post_bp = Blueprint('post',__name__,url_prefix='/post')


@post_bp.route('/create/<topic_id>',methods=['GET','POST'])
def create_post(topic_id):
    ''' Post Creation '''
    if 'username' not in session:
        return redirect('/login')
    else:
        if request.method == 'POST':
            try:
                print("hello?")
                user_query = db.session.execute(db.select(User).filter_by(username=session['username'])).scalar()
                new_post = Post(title=request.form["title"],meat_pot=request.form["wrds"],username=session['username'],category_id=topic_id)
                db.session.add(new_post)
                db.session.commit()
                return redirect("/")
            except Exception as e:
                return('<h1>500 An error has occured</h1>')
        else:
            try:
                return render_template('create_post.html',topic_id=topic_id)
            except Exception as e:
                return('<h1>404 Error couldnt reach page</h1>')

@post_bp.route('/view/<post_id>',methods=['GET','POST'])
def view_post(post_id):
    ''' view posts '''
    if 'username' not in session:
        return redirect('/login')
    else:
        try:
            post_query = db.session.execute(db.select(Post).filter_by(id=post_id)).scalar()
            result = post_query
            comment_query = db.session.execute(db.select(Comment).filter_by(post_id=post_id)).scalars()
            return render_template('view_post.html',result=result,comment_query=comment_query)
        except Exception as e:
            return('<h1>404 Error couldnt reach page </h1>')