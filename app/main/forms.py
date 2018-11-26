from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,ValidationError
from wtforms.validators import Required,Email 
from ..models import User,Pitch,Comment


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you',validators = [Required()])
    submit = SubmitField('submit')

class PitchForm(FlaskForm):
    category_id = SelectField('Category',choices=[("Pickup Lines","Pickup Lines"), ("Music", "Music"), ("Business", "Business"), ("Sports","Sports")])
    content = TextAreaField('submit your Pitch:')
    submit = SubmitField('Add Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment about the pitch:')
    submit = SubmitField('Add Comment')