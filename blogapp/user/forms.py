from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms.fields import SubmitField,StringField,PasswordField,RadioField
from wtforms.fields.html5 import DateField,EmailField,IntegerField
from wtforms.validators import DataRequired,Email,EqualTo,Length,ValidationError
from blogapp.user.models import UserModel
from flask_login import current_user
from operator import and_


# *********************************************FORMS************************************************
class UserLoginForm(FlaskForm):

    email=EmailField('email',validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField('login')

class UserSignupForm(FlaskForm):
    email=EmailField('email',validators=[DataRequired()])
    fname=StringField('first name',validators=[DataRequired()])
    lname=StringField('last name',validators=[DataRequired()])
    dob=DateField('date of birth',validators=[DataRequired()])
    mobile=IntegerField('mobile',validators=[DataRequired()])
    gender=RadioField('gender',choices=[('male','male'),('female','female'),('other','other')],coerce=str,validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    cpassword=PasswordField('confirm password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('signup')

    def validate_email(self,email):
        user=UserModel.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("email is already exits")

    def validate_mobile(self,mobile):
        user=UserModel.query.filter_by(mobile_no=mobile.data).first()
        if user:
            raise ValidationError("mobile is already exists")


class UpdateUserProfileForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(),Email()])
    profile_pic=FileField('upload profile pic',validators=[FileAllowed(['jpeg','jpg'])])
    fname=StringField('first name',validators=[DataRequired()])
    lname=StringField('last name',validators=[DataRequired()])
    dob=DateField('date of birth',validators=[DataRequired()])
    mobile=IntegerField('mobile',validators=[DataRequired()])
    gender=RadioField('gender',choices=[('male','male'),('female','female'),('other','other')],coerce=str,validators=[DataRequired()])
    submit=SubmitField('update')

    def validate_mobile(self,mobile):
        if current_user.mobile_no != str(mobile.data):
            user=UserModel.query.filter_by(mobile_no=mobile.data).first()
            if user:
                raise ValidationError("mobile is already exists")

    def validate_email(self,email):
        if current_user.email!=email.data:
            print(type(email.data))
            print(type(current_user.email))
            user=UserModel.query.filter_by(email=email.data).first()
            if user and user.email==email.data:
                raise ValidationError("email is already exists")