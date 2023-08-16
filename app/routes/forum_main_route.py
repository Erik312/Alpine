from flask import Blueprint,request,redirect,session,render_template
from app.models.db import db
from app.models.category_model import Category
from app.models.post_model import Post

forum_main_bp = Blueprint('forum',__name__,url_prefix='/forum')



@forum_main_bp.route('/')
def forum():
    ''' Forum main topic page '''
    if 'username' not in session:
        return redirect('/login')
    else:
        try:
            forum_topics = db.session.execute(db.select(Category).order_by(Category.id)).scalars()
            ft = forum_topics
            return render_template('forum_main.html',ft=ft )
        except Exception as e:
            return("<h1>404 Error couldnt reach page")
    
        
    
@forum_main_bp.route('forum/general/<topic_id>')
def general(topic_id):
    ''' forum General topic posts '''
    if 'username' not in session:
        return redirect('/login')
    else:
        try:
            query1 = db.session.execute(db.select(Post).filter_by(category_id=topic_id)).all()
            result = query1
            print(result)
            return render_template('general.html',result=result)
        except Exception as e:
            return("<h1>404 Error couldnt reach page</h1>")
        

#implement other forum topic routes like so
@forum_main_bp.route('forum/tech/<topic_id>')
def tech(topic_id):
    return