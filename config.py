# -*- coding: utf-8 -*-
DEBUG = True
SECRET_KEY = 'super-secret'

#info
SIET_TITLE = '测试'

# db
SQLALCHEMY_DATABASE_URI = 'postgresql://dbuser:3.1415926@localhost/testdb'
SQLALCHEMY_ECHO = False

# redis
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = 'wushuyi'
REDIS_DB = 0

# babel
BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'

# security
SECURITY_URL_PREFIX = "/auth"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"
SECURITY_TRACKABLE = True

SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"

SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
