from kaffelista import db
from kaffelista.models import User, Fika, Invoice, Purchase

counter = 0
list_users = []
list_price = []
for users in User.query.all():
    list_users.append(users)
    print(list_users)
for user in list_users:
    for purchase in Fika.query.all():
        prices = Fika.query.get(user.purchases[counter].type_of_fika).price
        list_price.append(prices)
        print(list_price)
        counter += 1



#prices = Fika.query.get(user.purchases[counter].type_of_fika).price