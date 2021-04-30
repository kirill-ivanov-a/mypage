from authlib.integrations.flask_client import OAuth
from flask import session, url_for
from loginpass import VK, create_flask_blueprint
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from models import VKUser

oauth = OAuth()
backends = [VK]


def vk_handle_authorize(remote, token, user_info):
    if user_info:
        vkuser = VKUser.query.filter(VKUser.vk_uid == user_info.get('sub')).first()
        if not vkuser:
            vkuser = create_vkuser(user_info)
            vkuser.save()
        session['vkuser'] = get_vkuserinfo(vkuser)
        return redirect(url_for('questions_page'))
    return abort(404)


def get_vkuserinfo(user):
    info = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'full_name': f'{user.first_name} {user.last_name}'
    }
    return info


def create_vkuser(user_info):
    return VKUser(vk_uid=user_info.get('sub'),
                  first_name=user_info.get('given_name'),
                  last_name=user_info.get('family_name'),
                  preferred_username=user_info.get('preferred_username'),
                  picture_url=user_info.get('picture'),
                  gender=user_info.get('gender'))


bp = create_flask_blueprint(backends, oauth, vk_handle_authorize)


@bp.route("/logout/vk")
def vk_logout():
    session.clear()
    return redirect(url_for('index_page'))
