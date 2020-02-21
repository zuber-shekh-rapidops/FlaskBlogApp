from blogapp import db
from datetime import datetime
from blogapp.post.models import PostModel

# **************************************************************MODELS*******************************************
class BlogModel(db.Model):
    __tablename__='blog'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),unique=True,nullable=False)
    creator_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    date_of_creation=db.Column(db.DateTime,default=datetime.now)
    is_active=db.Column(db.Boolean,default=False)
    posts=db.relationship('PostModel',backref='blog',lazy=True)

    def __repr__(self):
        return f"Blog : {self.name}"
    