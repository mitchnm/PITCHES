from ..models import User, Comments
from . import main
from flask import render_template, request, redirect, url_for, abort


@main.route("/")
def index():
    title = "Home"
    return render_template("index.html", title=title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)
