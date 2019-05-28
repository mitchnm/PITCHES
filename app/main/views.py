from ..models import User, Comments, Pitch
from . import main
from flask import render_template, request, redirect, url_for, abort
from .forms import UpdateProfile, DisplayPitch, CommentForm
from flask_login import login_required, current_user
from .. import db, photos

@main.route("/", methods=['GET', 'POST'])
def index():
    form = DisplayPitch()
    if form.validate_on_submit():
        category = form.categories.data
        pitch = form.text.data

        # Updated post
        new_pitch = Pitch(category=category, content=pitch, user=current_user)

        # save pitch method
        new_pitch.save_pitch()
     
    pitches = Pitch.query.all()
    title = "Home"
    return render_template('index.html', title=title, pitch_form=form, pitches=pitches)  

@main.route('/comments/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):

    form = CommentForm()
    comment = Comments.query.filter_by(id=id).first()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comments(comment=comment, user_id=current_user.id)
        new_comment.save_comment()
        return redirect(url_for('.comments', id=comment.id))

    title = "COMMENTS"   
    return render_template('index.html', comment=comment, comment_form=form, title=title)    
    
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile_page.html", user=user)

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))