import os

static_url_path = '/static'
instance_relative_config = True
SECRET_KEY = os.getenv('SECRET_KEY')
VK_CLIENT_ID = os.getenv('VK_CLIENT_ID')
VK_CLIENT_SECRET = os.getenv('VK_CLIENT_SECRET')
SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
FLASK_ADMIN_SWATCH = 'journal'
SECURITY_PASSWORD_HASH = 'sha512_crypt'
