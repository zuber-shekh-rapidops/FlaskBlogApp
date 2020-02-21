from flask import Blueprint,render_template,redirect,url_for,flash,request
from blogapp import db
from blogapp.user.forms import UserLoginForm,UserSignupForm,UpdateUserProfileForm
from blogapp.user.models import UserModel
from flask_login import login_user,current_user,logout_user,login_required

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

    if form.validate_on_submit():
        user.first_name=form.fname.data
        user.last_name=form.lname.data
        user.gender=form.gender.data
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