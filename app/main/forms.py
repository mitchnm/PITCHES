from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, RadioField
from wtforms.validators import Required

class DisplayPitch(FlaskForm):
    categories = RadioField('Select your preffered category', choices=[('qq', 'qq'), ('ww','ww'), ('rr', 'rr')])
    text = TextAreaField('Type in your pitch')
    submit = SubmitField('post')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')
