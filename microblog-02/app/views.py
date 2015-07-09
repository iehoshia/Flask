from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Josias'}
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Hoy es una bella tarde' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'La pelicula es bonita!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)
