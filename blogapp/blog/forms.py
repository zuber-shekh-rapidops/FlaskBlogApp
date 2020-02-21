from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,ValidationError
from blogapp.blog.models import BlogModel

# ********************************************FORMS***************************************************
class CreateBlogForm(FlaskForm):

    name=StringField('blog name',validators=[DataRequired()])
    submit=SubmitField('create')


    def validate_name(self,name):
        blog=BlogModel.query.filter_by(name=name.data).first()
        if blog:
            raise ValidationError("blog name is already taken!")