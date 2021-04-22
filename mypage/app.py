from flask import Flask
from flask_security import Security, SQLAlchemySessionUserDatastore
from database import db_session, init_db
from models import User, Role
from admin import admin
from vk_auth import oauth, bp as vk_bp

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)
admin.init_app(app)
oauth.init_app(app)
init_db()

user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
security = Security(app, user_datastore)

import views
import vk_auth

app.register_blueprint(vk_bp, url_prefix='')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
