from flask import Flask, render_template, url_for, flash, redirect

from forms import Registration_form, Signin_form

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY']= 'b95cdeda326355d16bc1a85e8877a88e'
### DAtabase Location
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)


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


posts= [
    {'author':'David copperfield',
     'title': 'Book',
     'content': 'novel',
     'date_posted':'April 12, 1896'},
    {'author':'David copperfield',
     'title': 'Book',
     'content': 'novel',
     'date_posted':'April 12, 1896'

    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts= posts)

@app.route('/about')
def about():
    return render_template('about.html', title= 'About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Registration_form()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')### Flash meassage
        return redirect(url_for('home'))


    return render_template('register.html', title= 'Register', form= form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form= Signin_form()
    if form.validate_on_submit():
        if form.email.data == 'admin@form.com' and form.password.data =="password":
            flash(f'You have been logged in as  {form.email.data}!', 'success')### Flash meassage
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check email or password', 'danger')
    return render_template('signin.html', tilte='SignIn', form= form)

if __name__ =='__main__':
    app.run(debug=True)