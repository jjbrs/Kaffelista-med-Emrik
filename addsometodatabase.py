import os
from kaffelista import db, bcrypt
from kaffelista.models import User, Purchase, Invoice, Fika

try:
    os.remove('kaffelista/site.db')
    print('previous DB file removed')
except:
    print('no previous file found')

db.create_all()

#Fika database
fika=Fika(name_of_fika='Kaffe', price=2)
db.session.add(fika)

fika=Fika(name_of_fika='Kaffe med mjölk', price=3)
db.session.add(fika)

fika=Fika(name_of_fika='Te', price=2)
db.session.add(fika)

fika=Fika(name_of_fika='Te med mjölk', price=3)
db.session.add(fika)

fika=Fika(name_of_fika='Kaka', price=2)
db.session.add(fika)

#fika=Fika(name_of_fika='Allt på en gång', price=5)
#db.session.add(fika)

#User database
hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
default_user1=User(username='johannatest', first_name='johanna', last_name='souza', email='test1@mail.com', password=hashed_password)
db.session.add(default_user1)

hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
default_user2=User(username='emriktest', first_name='emrik', last_name='larsson', email='test2@mail.com', password=hashed_password, userlevel=1)
db.session.add(default_user2)

hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
default_user3=User(username='tomten', first_name='Papa', last_name='Noel', email='nordpolen@mail.com', password=hashed_password, userlevel=0)
db.session.add(default_user3)


#Purchase Database
purchase=Purchase(user=default_user1, type_of_fika=1)
db.session.add(purchase)

purchase=Purchase(user=default_user1, type_of_fika=1)
db.session.add(purchase)

purchase=Purchase(user=default_user1, type_of_fika=1)
db.session.add(purchase)

purchase=Purchase(user=default_user1, type_of_fika=1)
db.session.add(purchase)

purchase=Purchase(user=default_user2, type_of_fika=2)
db.session.add(purchase)

purchase=Purchase(user=default_user2, type_of_fika=2)
db.session.add(purchase)

purchase=Purchase(user=default_user2, type_of_fika=2)
db.session.add(purchase)

purchase=Purchase(user=default_user2, type_of_fika=2)
db.session.add(purchase)

purchase=Purchase(user=default_user3, type_of_fika=1)
db.session.add(purchase)

purchase=Purchase(user=default_user3, type_of_fika=2)
db.session.add(purchase)

purchase=Purchase(user=default_user3, type_of_fika=1)
db.session.add(purchase)

purchase=Purchase(user=default_user3, type_of_fika=2)
db.session.add(purchase)

purchase=Purchase(user=default_user3, type_of_fika=1)
db.session.add(purchase)

#Invoice database, value 0 = Not payed, value 1 = Payed
invoice=Invoice(user=default_user1, month=1, year=2020, value=40, payment_status=1)
db.session.add(invoice)

invoice=Invoice(user=default_user1, month=2, year=2020, value=58, payment_status=1)
db.session.add(invoice)

invoice=Invoice(user=default_user1, month=3, year=2020, value=60, payment_status=0)
db.session.add(invoice)

invoice=Invoice(user=default_user2, month=1, year=2020, value=100, payment_status=1)
db.session.add(invoice)

invoice=Invoice(user=default_user2, month=2, year=2020, value=25, payment_status=0)
db.session.add(invoice)

invoice=Invoice(user=default_user2, month=3, year=2020, value=48, payment_status=0)
db.session.add(invoice)

invoice=Invoice(user=default_user3, month=1, year=2020, value=60, payment_status=1)
db.session.add(invoice)

invoice=Invoice(user=default_user3, month=2, year=2020, value=70, payment_status=0)
db.session.add(invoice)

invoice=Invoice(user=default_user3, month=3, year=2020, value=50, payment_status=0)
db.session.add(invoice)

db.session.commit()


