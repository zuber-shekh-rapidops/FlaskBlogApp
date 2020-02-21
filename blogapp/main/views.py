from flask import Blueprint,render_template,redirect,url_for
from flask_login import current_user

main=Blueprint('main',__name__)


@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('user.home'))
    return render_template('main/index.html')   