from app.models.db import db
from app.models.category_model import Category



def CatCreate():
    ''' Create forum topics Script. Runs when app is created.'''
    print("checking for forum categories")
    try:
        cat1 = Category(title='General',url_s="/general")
        cat2 = Category(title='Tech Tips',url_s="/tech" )
        cat3 = Category(title='Swapmeet',url_s="/swapmeet")
        cat4 = Category(title='bugs',url_s="/bugs")
        cat5 = Category(title='About Alpine',url_s="/about")
        db.session.add_all([cat1,cat2,cat3,cat4,cat5])
        db.session.commit()
        print("Topic Categories Created")
    except Exception as e:
        print(e)
        print("error creating categories. Categories likely already exist")
        return