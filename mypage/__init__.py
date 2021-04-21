from flask import Flask
from flask_security import Security, SQLAlchemySessionUserDatastore
from mypage.database import db_session, Base
from mypage.models import VKUser, User, Role
from mypage.database import db_session
from mypage.database import init_db
from mypage.admin import admin
from mypage.vk_auth import oauth, bp as vk_bp

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)
admin.init_app(app)
oauth.init_app(app)
init_db()

user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
security = Security(app, user_datastore)

import mypage.views
import mypage.vk_auth

app.register_blueprint(vk_bp, url_prefix='')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
