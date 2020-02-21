from flask import Blueprint,render_template,redirect,url_for,flash,request
from blogapp import db
from blogapp.post.forms import AddPostForm
from blogapp.post.models import PostModel
from flask_login import login_required

post=Blueprint('post',__name__,url_prefix='/post')


@post.route('/<int:id>')
@login_required
def view_post(id):
    post=PostModel.query.get_or_404(id)
    return render_template('post/post.html',post=post)

@post.route('/create/<int:id>',methods=['GET','POST'])
@login_required
def create_post(id):
    form=AddPostForm()
    if form.validate_on_submit():
        post=PostModel(title=form.title.data,content=form.content.data,blog_id=id)
        db.session.add(post)
        db.session.commit()
        flash("post created successfully!")
        return redirect(url_for('blog.view_blog',id=id))
    return render_template('post/create_post.html',form=form,form_title='create new post')

@post.route('/update/<int:id>',methods=['GET','POST'])
@login_required
def update_post(id):
    post=PostModel.query.get_or_404(id)
    form=AddPostForm()
    if request.method=='GET':
        form.title.data=post.title
        form.content.data=post.content
        form.submit.label.text='update'

    if form.validate_on_submit():
        post.title=form.title.data
        post.content=form.content.data
        db.session.commit()
        flash('post updated successfully!')
        return redirect(url_for('post.view_post',id=id))
        
    return render_template('post/create_post.html',form=form,form_title='update post')
