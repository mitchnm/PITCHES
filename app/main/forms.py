from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class DisplayPitch(FlaskForm):
    text = TextAreaField('Type in your pitch', validators=[Required()])
    categories = SelectField('Select your preffered category', choices=[('HUMOR', 'HUMOR'), ('BUSINESS', 'BUSINESS'), ('INSPIRATIONAL', 'INSPIRATIONAL'), ('SPIRITUAL', 'SPIRITUAL')])
    submit = SubmitField('post')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Add a comment.', validators=[Required()])
    submit = SubmitField('Submit')
