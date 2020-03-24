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


hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
default_user1=User(username='johannatest', first_name='johanna', last_name='souza', email='test@mail.com', password=hashed_password)
db.session.add(default_user1)

db.session.commit()






#def createFika():
  # name_of_fika = ['kaffe', 'kaffe+mjölk', 'te', 'te+mjölk', 'kaka']
  # price = [2,3,2,3,2]

   #for i in range(2):
    #   fika = Fika(name_of_fika=name_of_fika[i], price = price[i])
     #  db.session.add(fika)
