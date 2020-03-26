from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from sqlalchemy import event
import datetime



app = Flask(__name__)
app.config['SECRET_KEY'] = '42b91f0708b26ae05c592eb5c0fe075e'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # option to be used during the development phase, prevents caching

app.config['SQLALCHEMY_ECHO'] = True # option for debugging -- should be set to False for production


def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute('pragma foreign_keys=ON')

db = SQLAlchemy(app)

event.listen(db.engine, 'connect', _fk_pragma_on_connect)


@app.before_request
def before():
    if request.path.startswith('/api') \
            and request.path != '/api/token/public':
        # if the request goes to the API, and is different from the one to get a token, token should match
        if request.is_json and 'Authorization' in request.headers: # only JSON requests are allowed
            from kaffelista.models import Token
            token_string = request.headers['Authorization'].split(' ')[1]
            token = db.session.query(Token).filter_by(token=token_string).all()
            now = datetime.datetime.now()
            if len(token) == 0:
                abort(403)
            elif token[0].date_expired < now:
                abort(403)
        else:
            return abort(403)

    # limiting the addresses
    if not request.remote_addr.startswith('127.0.0') and not request.remote_addr.startswith('129.16.'):
        print('DENIED:', request.remote_addr, request.headers)
        abort(403) # forbidden


# option to be used during the development phase, prevents caching
# comment when using it in production
# for more info check: https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.after_request
# and https://stackoverflow.com/questions/34066804/disabling-caching-in-flask
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'



from kaffelista import routes