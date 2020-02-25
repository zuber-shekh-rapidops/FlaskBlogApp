from flask import Blueprint,render_template,flash,redirect,url_for,request,abort
from blogapp import db
from blogapp.blog.models import BlogModel
from blogapp.blog.forms import CreateBlogForm
from blogapp.post.models import PostModel
from flask_login import current_user,login_required

blog=Blueprint('blog',__name__,url_prefix='/blog')


@blog.route('/all')
def blogs():
    blogs=BlogModel.query.filter_by(is_active=True).order_by(BlogModel.date_of_creation.desc()).all()
    return render_template('blog/blogs.html',blogs=blogs)

@blog.route('/<int:id>')
@login_required
def view_blog(id):
    blog=BlogModel.query.get_or_404(id)
    if current_user.username!=blog.creator.username:
        abort(403)
    return render_template('blog/blog.html',blog=blog)

@blog.route('/create',methods=['GET','POST'])
@login_required
def create_blog():
    form=CreateBlogForm()
    if form.validate_on_submit():
        blog=BlogModel(name=form.name.data,creator_id=current_user.id)
        db.session.add(blog)
        db.session.commit()
        flash('blog created successfully')
        return redirect(url_for('user.home'))

    return render_template('blog/create_blog.html',form=form)

@blog.route('/status/<int:id>')
@login_required
def change_blog_status(id):
    blog=BlogModel.query.get_or_404(id)
    if blog.is_active:
        blog.is_active=False
    else:
        blog.is_active=True
    db.session.commit()
    return redirect(url_for('blog.view_blog',id=blog.id))


@blog.route('/edit/<int:id>',methods=['GET','POST'])
@login_required
def update_blog(id):
    form=CreateBlogForm()
    blog=BlogModel.query.get_or_404(id)
    if request.method=='GET':
        form.name.data=blog.name
        form.submit.label.text='update'

    if form.validate_on_submit():
        blog.name=form.name.data
        db.session.commit()
        return redirect(url_for('blog.view_blog',id=id))

    return render_template('blog/create_blog.html',form=form)


@blog.route('/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete_blog(id):
    blog=BlogModel.query.get_or_404(id)

    if blog:
        db.session.delete(blog)
        db.session.commit()
        return redirect(url_for('user.home'))