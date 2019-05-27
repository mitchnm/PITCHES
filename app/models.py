from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from sqlalchemy import func

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    pitches = db.relationship("Pitch", backref="user", lazy="dynamic")
    Comments = db.relationship("Comments", backref="user", lazy="dynamic")
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    """
    This is the class which we will use to create the pitches for the app
    """
    __tablename__ = "pitches"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    date = db.Column(db.String)
    time = db.Column(db.DateTime ,index=True, default=func.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    Comments = db.relationship("Comments", backref="pitch", lazy="dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def get_pitch_comments(self):
        pitch = Pitch.query.filter_by(id=self.id).first()
        comments = Comments.query.filter_by(pitch_id=pitch.id).order_by(Comments.time.desc())
        return comments

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))   
    date = db.Column(db.String)
    time = db.Column(db.String)
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

class Categories(db.Model):
    __tablename__ = 'categories'

    id =db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))


    def save_categories(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = Categories.query.all()
        return categories