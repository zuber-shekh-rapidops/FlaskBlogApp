# ****************************************************IMPORTS****************************************************
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# ****************************************************CONFIGURATIONS****************************************************
basedir=os.path.abspath(os.path.dirname(__name__))
app=Flask(__name__)
app.config['SECRET_KEY']='secret123'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db=SQLAlchemy(app)
Migrate(app,db)
login_manager=LoginManager(app)
bcrypt=Bcrypt(app)


# ****************************************************BLUEPRINTS****************************************************
from blogapp.main.views import main
from blogapp.user.views import user
from blogapp.post.views import post
from blogapp.blog.views import blog

app.register_blueprint(main)
app.register_blueprint(user)
app.register_blueprint(post)
app.register_blueprint(blog)

# ****************************************************VIEWS/ROUTES****************************************************
from blogapp.main import views
from blogapp.user import views
from blogapp.post import views