from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,ValidationError
from ,wtforms.validators import Required,Email 
from ..models import User,Pitch,Comment,Upvote,Downvote


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you',validators = [Required()])
    submit = SubmitField('submit')

class PitchForm(FlaskForm):
    category_id = SelectField('Select Category :', choices = [('Pickup LInes', 'Pickup Lines'),('')])
    content = TextAreaField('submit your Pitch:')
    submit = SubmitField('Add Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment about the pitch:')
    submit = SubmitField('Add Comment')