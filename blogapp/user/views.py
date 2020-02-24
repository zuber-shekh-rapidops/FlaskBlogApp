from flask import Blueprint,render_template,redirect,url_for,flash,request
from blogapp import db,app
from blogapp.user.forms import UserLoginForm,UserSignupForm,UpdateUserProfileForm
from blogapp.user.models import UserModel
from flask_login import login_user,current_user,logout_user,login_required
from PIL import Image
import secrets
import os

user=Blueprint('user',__name__,url_prefix='/user')

@user.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.home'))

    form=UserLoginForm()
    if form.validate_on_submit():
        user=UserModel.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('login successfully!')
            return redirect(url_for('user.home'))
        flash('invalid email or password')
        return redirect(url_for('user.login'))
    return render_template('user/login.html',form=form)

@user.route('/signup',methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('user.home'))

    form=UserSignupForm()
    if form.validate_on_submit():
        user=UserModel(email=form.email.data,
        first_name=form.fname.data,
        last_name=form.lname.data,
        mobile_no=form.mobile.data,
        gender=form.gender.data,
        password=form.password.data,
        dob=form.dob.data)
        db.session.add(user)
        db.session.commit()
        flash("Your account is created!")
        return redirect(url_for('user.login'))

    return render_template('user/signup.html',form=form)

@user.route('/home')
@login_required
def home():
    return render_template('user/home.html')

# HOW TO SAVE PROFILE PICTURE 
def save_picture(image_file):
    output_size=(200,200)
    random_hex=secrets.token_hex(8)
    i=Image.open(image_file)
    i.thumbnail(output_size)
    _,file_ext=os.path.splitext(image_file.filename)
    picture_file=random_hex+file_ext
    picture_path=os.path.join(app.root_path,'static/images/profile_pics',picture_file)
    i.save(picture_path)
    return picture_file

@user.route('/update/<int:id>',methods=['GET','POST'])
@login_required
def update_profile(id):
    user=UserModel.query.get_or_404(id)
    form=UpdateUserProfileForm()
    if request.method=='GET':
        form.fname.data=user.first_name
        form.lname.data=user.last_name
        form.gender.data=user.gender
        form.dob.data=user.dob
        form.mobile.data=user.mobile_no
        form.email.data=user.email
        form.profile_pic.data=user.profile_pic
        profile_name=user.profile_pic

    if form.validate_on_submit():
        if form.profile_pic.data:
            image=save_picture(form.profile_pic.data)
            user.profile_pic=image
        user.first_name=form.fname.data
        user.last_name=form.lname.data
        user.gender=form.gender.data
        user.mobile_no=form.mobile.data
        user.email=form.email.data
        db.session.commit()
        flash('your prfile is updated!')
        return redirect(url_for('user.home'))
    return render_template('user/update_profile.html',form=form)

@user.route('/logout')
@login_required
def logout():
    logout_user()
    flash("logout successfully")
    return redirect(url_for('user.login'))