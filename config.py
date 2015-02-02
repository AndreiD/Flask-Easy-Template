import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = ''
    APP_NAME = 'Flask Easy-Template'
    SECRET_KEY = 'write-a-secret-string-here!@#$'
    LISTINGS_PER_PAGE = 100

    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    SECURITY_PASSWORD_SALT = 'add_salt_123_hard_one'
    SECURITY_CONFIRMABLE = True

    #-- you can also use Sendgrid.com for 200 email per day (free)
    MAIL_SERVER = 'smtp.mail.yahoo.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'user@yahoo.com'
    MAIL_PASSWORD = 'password'
    DEFAULT_MAIL_SENDER = 'user@yahoo.com'
    SECURITY_EMAIL_SENDER = 'user@yahoo.com'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user:pass@server_ip:server_port/db_name'
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    TESTING = True
