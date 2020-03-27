from kaffelista import db
from kaffelista.models import User, Fika, Invoice, Purchase
import datetime

counter = 0
list_users = []
list_price = []
for users in User.query.all():
    list_users.append(users)
    print(list_users)
for user in list_users:
    print(user)
    counter=0
    for purchase in Purchase.query.filter_by(user=user).all():
        prices = Fika.query.get(user.purchases[counter].type_of_fika).price
        list_price.append(prices)
        counter += 1
        summa=sum(list_price)
        invoice = Invoice(user=user, month=3, year=2020, value=summa, payment_status=0)
    db.session.add(invoice)
    db.session.commit()
    print("listan", list_price)
    summa = sum(list_price)
    print("totala summan", summa)
    print(invoice)
    list_price.clear()
