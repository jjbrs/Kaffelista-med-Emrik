from flask import render_template, url_for, flash, redirect, request

from kaffelista import app, db, bcrypt
from kaffelista.forms import RegistrationForm, LoginForm, UpdateAccountForm, FikaForm
from kaffelista.models import User, Fika, Purchase, Invoice
from flask_login import login_user, current_user, logout_user, login_required



@app.route("/")
#def hello():
#    return '<h1>Fikadags!</h1>'
@app.route("/home")
def home():
    return render_template('home.html', title='Hem')


@app.route("/about")
def about():
    return render_template('about.html', title='Om')


@app.route("/register", methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, first_name=form.first_name.data, last_name = form.last_name.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}, you can now login!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)


@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('fika'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next') #KOLLA OM DETTA ÄR NÖDVÄNDIGT FÖR OSS
            return redirect(url_for('fika')) #HÄNGER IHOP MED FÖREGÅENDE RAD redirect(next_page) if next_page else
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods = ['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
    return render_template('account.html', title='Account', form=form)



@app.route("/fika", methods = ['GET', 'POST'])
@login_required
def fika():
    form = FikaForm()
    if form.validate_on_submit():
        fika = Fika.query.get('fika.id') # Tror det är här den ska hämta det som valdes i FikaForm och sedan lägga till i 'purchase',
                                        # att där är "fika=valet i FikaForm. Och vi behöver koppla då valen till de olika 'id' som hänger ihop med Fika
        purchase=Purchase(fika=fika, type_of_fika=form.type_of_fika.data, user=current_user)
        db.session.add(purchase)
        db.session.commit()
        flash('Du har nu köpt lite fika!', 'info')
    return render_template('fika.html', title='Fika', form=form)
