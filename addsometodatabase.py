import os
from kaffelista import db, bcrypt
from kaffelista.models import User, Purchase, Invoice, Fika

try:
    os.remove('kaffelista/site.db')
    print('previous DB file removed')
except:
    print('no previous file found')

db.create_all()

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

fika=Fika(name_of_fika='Allt på en gång', price=5)
db.session.add(fika)


hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
default_user1=User(username='johannatest', first_name='johanna', last_name='souza', email='test1@mail.com', password=hashed_password)
db.session.add(default_user1)

hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
default_user2=User(username='emriktest', first_name='emrik', last_name='larsson', email='test2@mail.com', password=hashed_password, userlevel=1)
db.session.add(default_user2)

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

invoice=Invoice()

db.session.commit()


