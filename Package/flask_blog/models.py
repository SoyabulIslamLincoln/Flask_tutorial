from flask_blog import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    user_name = db.Column(db.String(35), unique = True, nullable= False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    image_file = db.Column(db.String(30), nullable= False, default='default.jpg')
    password = db.Column(db.String(50), nullable= False)

    posts = db.relationship('Post', backref='author', lazy= True )


    def __repr__(self):
        return f"User('{self.user_name}', '{self.email}', '{self.image_file}')"



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable = False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"