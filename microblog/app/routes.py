from flask.helpers import url_for
from app import app
from flask import render_template
from app.forms import LoginForm
from flask import render_template, flash, redirect
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required

from app import db
from app.forms import RegistrationForm


# Create Log out function 
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# create our first view and give this view two paths the first path which is the main path is '/' the second path '/index'
@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template('index.html',title='Home',posts=posts)


# Create login form view
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)



#  Create register form View
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)