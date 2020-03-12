from flask import render_template, url_for, flash, redirect
from kaffelista import app
from kaffelista.forms import RegistrationForm, LoginForm
from kaffelista.models import User, Fika, Purchase, Invoice



@app.route("/")
def hello():
    return '<h1>BAJSKORV!</h1>'


@app.route("/home")
def home():
    return render_template('home.html', title='Hem')


@app.route("/about")
def about():
    return render_template('about.html', title='Om')


@app.route("/register")
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)