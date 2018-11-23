from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

   
    @property
    def password(self):
         raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'{self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    users = db.relationship('User', backref='pitch', lazy='dynamic')

   
    def save_pitch(self):
        '''
        Function that saves all pitches posted
        '''
        db.session.add(self)
        db.session.commit()

@classmethod
def get_all_pitches(cls):
        '''
        Function that queries database and returns all posted pitches.
        '''
        return Pitch.query.all()

@classmethod
def get_pitches_by_category(cls,category_id):
        '''
        Function that queries the database and returns all pitches per category passed.
        '''
        return Pitch.query.filter_by(category_id = category_id)


class Category(db.Model):
    '''
    Function that will define all the different categories of pitches.
    '''
    __tablename__ ='categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(255))
    category_description = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='category', lazy='dynamic')


    @classmethod
    def get_categories(cls):
        '''
        Function that queries the database and returns all the categories from the database
        '''
        categories = Category.query.all()
        return categories


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment=db.Column(db.String(255))
    username =db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    pitches = db.relationship('Pitch', backref='comment', lazy='dynamic')



    def save_comment(self):
        '''
        Function that saves all comments made on a pitch
        '''
        db.session.add(self)
        db.session.commit()

@classmethod
def clear_comments(cls):
        Comment.all_comments.clear()

@classmethod
def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()

        return comments
