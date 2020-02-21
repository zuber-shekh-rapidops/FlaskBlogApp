from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length


# ***********************************FORMS********************************************
class AddPostForm(FlaskForm):

    title=StringField('post title',validators=[DataRequired()])
    content=TextAreaField('post content',validators=[DataRequired(),Length(min=20,max=200)])
    submit=SubmitField('create')