from flask_wtf import FlaskForm
from wtforms.fields import SubmitField,StringField,PasswordField,RadioField
from wtforms.fields.html5 import DateField,EmailField,IntegerField
from wtforms.validators import DataRequired,Email,EqualTo,Length,ValidationError
from blogapp.user.models import UserModel


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
    fname=StringField('first name',validators=[DataRequired()])
    lname=StringField('last name',validators=[DataRequired()])
    dob=DateField('date of birth',validators=[DataRequired()])
    gender=RadioField('gender',choices=[('male','male'),('female','female'),('other','other')],coerce=str,validators=[DataRequired()])
    submit=SubmitField('update')

    def validate_mobile(self,mobile):
        user=UserModel.query.filter_by(mobile_no=mobile.data).first()
        if user:
            raise ValidationError("mobile is already exists")