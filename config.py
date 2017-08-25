# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
TRANSLATE_API_KEY = 'trnsl.1.1.20170808T170001Z.5951de3f4cdf4c89.6ed2a4c048e8468d7d712f6a0f5ac3bfb55011e4'

# available languages
LANGUAGES = {
    'en': 'English',
    'ru': 'Русский'
}

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50
OAUTH_CREDENTIALS = {'facebook': {'id': '1720135821333142', 'secret': '1dd652b1806d90651bc0f84ccaef5c8c'}, 'Vk': {'id': '6151748', 'secret': 'RJ5ZbjzpjOF8LV1zWg9k'} }

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
#MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
#MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_USERNAME = 'zy964c@gmail.com'
MAIL_PASSWORD = 'Bvcxz123'

# administrator list
ADMINS = ['zy964c@gmail.com']

# pagination
POSTS_PER_PAGE = 10
