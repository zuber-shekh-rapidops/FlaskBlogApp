from blogapp import db,bcrypt,login_manager
from flask_login import UserMixin
from blogapp.blog.models import BlogModel
    
# **************************************MODELS******************************************************
@login_manager.user_loader
def load_user(id):
    return UserModel.query.get(int(id))  

class UserModel(db.Model,UserMixin):

    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(20),unique=True,nullable=False)
    password=db.Column(db.String(256),nullable=False)
    first_name=db.Column(db.String(20),nullable=False)
    last_name=db.Column(db.String(20),nullable=False)
    dob=db.Column(db.DateTime,nullable=False)
    gender=db.Column(db.String,nullable=False)
    mobile_no=db.Column(db.String(10),unique=True,nullable=False)
    blogs=db.relationship('BlogModel',backref='creator',lazy=True)
    
    def __init__(self,email,password,first_name,last_name,mobile_no,gender,dob):
        self.username=str(email).split('@')[0]
        self.email=email
        self.password=bcrypt.generate_password_hash(password).decode('utf-8')
        self.first_name=first_name
        self.last_name=last_name
        self.mobile_no=mobile_no
        self.gender=gender
        self.dob=dob

    def __repr__(self):
        return f"Hello I am {self.username}"

    def check_password(self,password):
        return bcrypt.check_password_hash(self.password,password)
