from flask_blog.models import User, Post
from flask import  render_template, url_for, flash, redirect
from flask_blog.forms import Registration_form, Signin_form
from flask_blog import app
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
