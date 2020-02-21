from blogapp import db
from datetime import datetime

# ***************************************************MODELS********************************************************
class PostModel(db.Model):

    __tablename__='post'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    content=db.Column(db.Text,nullable=False)
    created_on=db.Column(db.DateTime,default=datetime.now)
    blog_id=db.Column(db.Integer,db.ForeignKey('blog.id'))


    def __repr__(self):
        return f"post : {self.title}"