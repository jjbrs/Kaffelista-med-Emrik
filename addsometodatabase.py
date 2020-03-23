from kaffelista import db
from kaffelista.models import User, Purchase, Invoice, Fika

def createFika():
   name_of_fika = ["Kaffe", "Te", "Mjölk", "Kaka"]
   price = [2,2,1,2]

   for i in range(2):
       fika = Fika(name_of_fika=name_of_fika[i], price = price[i])
       db.session.add(fika)