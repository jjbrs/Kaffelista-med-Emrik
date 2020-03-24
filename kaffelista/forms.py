
from flask_wtf import FlaskForm
#from flask.wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from kaffelista.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    first_name = StringField('First Name', validators=[DataRequired(),Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    user_type=BooleanField('Admin?')
    submit=SubmitField('Lets start to fika!')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username already exist, pick another username')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email already exist, use another one')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
    
    
class FikaForm(FlaskForm): #This is the choises we want to display for the user:
    type_of_fika=RadioField('Fika val', choices=[('kaffe', 'Kaffe'), ('kaffe+mjölk', 'Kaffe med mjölk'), ('te', 'Te'), ('te+mjölk', 'Te med mjölk'), ('kaka', 'Kaka')])
    submit = SubmitField('Bekräfta köp')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    first_name = StringField('First Name', validators=[DataRequired(),Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    submit=SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username: #detta är för att kunna uppdatera användarnamn och email (koden nedaför,)
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username already exist, pick another username')


    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email already exist, use another one')


class PurchaseForm(FlaskForm): #This is the same as FikaForm
    kaffe = IntegerField('Kaffe:', default=0)
    milk = IntegerField('Mjölk:', default=0)
    te = IntegerField('Te:', default=0)
    kaka = IntegerField('Kaka:', default=0)
    submit = SubmitField('Bekräfta val')
