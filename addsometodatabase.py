import os
from kaffelista import db
from kaffelista.models import User, Purchase, Invoice, Fika


try:
    os.remove('kaffelista/site.db')
    print('previous DB file removed')
except:
    print('no previous file found')

db.create_all()

fika_kaffe=Fika(name_of_fika='Kaffe', price=2)
db.session.add(fika_kaffe)

fika_kaffe_m_mjolk=Fika(name_of_fika='Kaffe med mjölk', price=3)
db.session.add(fika_kaffe_m_mjolk)

fika_te=Fika(name_of_fika='Te', price=2)
db.session.add(fika_te)

fika_te_m_mjolk=Fika(name_of_fika='Te med mjölk', price=3)
db.session.add(fika_te_m_mjolk)

fika_kaka=Fika(name_of_fika='Kaka', price=2)
db.session.add(fika_kaka)


hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
default_user1=User(username='johannatest', first_name='johanna', last_name='souza',
                   email='test@mail.com', password=hashed_password)
db.session.add(default_user1)

db.session.commit()











#def createFika():
#   name_of_fika = ["Kaffe", "Te", "Mjölk", "Kaka"]
#   price = [2,2,1,2]

#   for i in range(2):
#       fika = Fika(name_of_fika=name_of_fika[i], price = price[i])
#       db.session.add(fika)
