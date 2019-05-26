from ..models import User, Comments
from . import main
from flask import render_template, redirect


@main.route("/")
def index():
    title = "Home"
    return render_template("index.html", title=title)
