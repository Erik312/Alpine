from flask import Blueprint,render_template,request,redirect,session
from app.models.db import db
from app.models.comments_model import Comment



comment_bp = Blueprint('comment',__name__,url_prefix='/comment')



@comment_bp.route('/create/<post_id>',methods=['GET','POST'])
def comment(post_id):
    ''' Comment creation route '''
    if 'username' not in session:
        return redirect('/login')
    else:
        if request.method == "POST":
            try:
                new_comment = Comment(meat_pot=request.form['lrg_mp'],username=session['username'],post_id=post_id)
                db.session.add(new_comment)
                db.session.commit()
                return redirect(f'/post/view/{post_id}')
            except Exception as e:
                return(e,":error creating comment")
        else:
            try:
                return render_template('create_comment.html',post_id=post_id)
            except Exception as e:
                return("<h1> 404 couldnt reach page try again later.</h1>")
            
    
