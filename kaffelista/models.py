from datetime import datetime
from kaffelista import db, login_maganer
from flask_login import UserMixin

@login_maganer.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    user_type = db.Column(db.String(10), nullable = False) # nu ser den ut såhär: user_type = db.Column(db.Integer()) # Har ändrat till integer istället för en string plus att jag har tagit bort 'nullable=False'
    invoices = db.relationship('Invoice', backref='customer', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.first_name}', '{self.last_name}')"

class Fika(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    name_of_fika = db.Column(db. String(20), nullable=False)
    price = db.Column(db.Float(20), nullable = False)

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    user_id = db. Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    user = db.relationship(User)
    fika_id = db.Column(db.Integer, db.ForeignKey('fika.id'), nullable = False)
    fika = db.relationship(Fika)
    type_of_fika = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Integer)
    date_of_purchase = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User)
    month = db.Column(db.Integer(), nullable = False)
    year = db.Column(db.Integer(), nullable = False)
    value = db.Column(db.Integer)
    payment_status = db.Column(db.Integer)

