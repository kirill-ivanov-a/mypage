from flask import url_for, request
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from werkzeug.utils import redirect

from mypage.database import db_session
from mypage.models import Question, Answer, VKUser


class HomeAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class AdminView(ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('index_page'))


admin = Admin(name='Mypage admin panel', template_mode='bootstrap4',
              index_view=HomeAdminView(name='Home'))
admin.add_view(AdminView(VKUser, db_session))
admin.add_view(AdminView(Question, db_session))
admin.add_view(AdminView(Answer, db_session))
