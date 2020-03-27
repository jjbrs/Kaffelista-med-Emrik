from flask import request, jsonify, abort, make_response, Response
from kaffelista import app, db, bcrypt
from kaffelista.models import Token, Fika, User, Purchase
import datetime


# method used to create a token that can be used for some time defined by the delta
@app.route('/api/token/public', methods=['GET'])
def token():
    expired = datetime.datetime.now() + datetime.timedelta(minutes=60)
    token_string = bcrypt.generate_password_hash(str(expired)).decode('utf-8')
    new_token = Token(token=token_string, date_expired=expired)
    db.session.add(new_token)
    try:
        db.session.commit()
        return jsonify({'token': token_string, 'expire': expired.strftime('%Y-%m-%d %H:%M:%S')})
    except:
        db.session.rollback()
        return abort(400)


# method used to inform the user of the webservice regarding its capabilities
@app.route('/api/', methods=['GET'])
def api():
    info = dict()
    info['message'] = 'This is the API to consume blog posts'
    info['services'] = []
    info['services'].append({'url': '/api/purchase', 'method': 'GET', 'description': 'Gets a list of purchases'})
    print(info)
    return jsonify(info)


@app.route('/api/users', methods=['GET'])
def api_get_users():
    users = User.query.all()
    return jsonify(users)


@app.route('/api/purchases', methods=['GET'])
def api_get_purchases():

    purchases = Purchase.query.all()
    return jsonify(purchases)


@app.route('/api/purchase/<int:purchase_id>', methods=['GET'])
def api_get_purchase(purchase_id):
    purchase = Purchase.query.get_or_404(purchase_id)
    return jsonify(purchase)


@app.route('/api/purchase', methods=['POST'])
def api_create_purchase():
    data = request.json
    if 'type_of_fika' in data and 'user' in data:
        purchase = Purchase(type_of_fika=data['type_of_fika'],
                            user_id=int(data['user']),
                            date_of_purchase=datetime.datetime.utcnow)
        db.session.add(purchase)
        try:
            db.session.commit()  # how would you improve this code?
            return jsonify(purchase), 201  # status 201 means "CREATED"
        except:
            db.session.rollback()
            abort(400)
    else:
        return abort(400)  # 400 is bad request


# method PUT replaces the entire object
@app.route('/api/purchase/<int:purchase_id>', methods=['PUT'])
def api_update_purchase(purchase_id):
    purchase = Purchase.query.get_or_404(purchase_id)
    data = request.json
    if 'type_of_fika' in data and 'user' in data:
        purchase.type_of_fika = data['type_of_fika']
        purchase.user_id = data['user']
        try:
            db.session.commit()
            return jsonify(purchase), 200
        except:
            db.sesion.rollback()
            abort(400)
    else:
        return abort(400)  # bad request


@app.route('/api/purchase/<int:purchase_id>', methods=['PATCH'])
def api_replace_purchase(purchase_id):
    purchase = Purchase.query.get_or_404(purchase_id)
    data = request.json
    # you should have at least one of the columns to be able to perform an update
    if 'type_of_fika' in data or 'user' in data:
        if 'type_of_fika' in data:
            purchase.type_of_fika = data['type_of_fika']
        if 'user' in data:
            purchase.user_id = data['user']
        try:
            db.session.commit()
            return jsonify(purchase), 200
        except:
            db.sesion.rollback()
            abort(400)
    else:
        return abort(400)  # bad request


@app.route('/api/purchase/<int:purchase_id>', methods=['DELETE'])
def api_delete_purchase(purchase_id):
    purchase = Purchase.query.get_or_404(purchase_id)
    db.session.delete(purchase)
    try:
        db.session.commit()
        return jsonify({'message': f'Purchase {purchase_id} deleted'}), 200
    except:
        db.session.rollback()
        abort(400)
