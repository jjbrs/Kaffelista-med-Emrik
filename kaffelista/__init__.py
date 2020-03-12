from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = '42b91f0708b26ae05c592eb5c0fe075e'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)

login_maganer = LoginManager(app)

from kaffelista import routes