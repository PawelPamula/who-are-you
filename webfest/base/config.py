"""Config app."""
import os


class Config(object):

    """General config."""

    EXTENSIONS = [
        'webfest.extensions.assets',
        'webfest.extensions.cache',
        'webfest.extensions.collect',
        'webfest.extensions.debug',
        'webfest.extensions.login',
        'webfest.extensions.sqlalchemy',
    ]

    PACKAGES = [
        'webfest.base'
    ]

    PACKAGES_EXCLUDE = []
    CACHE_TYPE = 'simple'


class ProdConfig(Config):

    """Production config."""


class HerokuConfig(Config):

    """Heroku config."""

    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    COLLECT_STORAGE = 'flask.ext.collect.storage.file'
    ASSETS_DEBUG = False


class DevConfig(Config):

    """Dev config."""

    DEBUG = True
    ASSETS_DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))

    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_ECHO = True
    WTF_CSRF_ENABLED = False
    COLLECT_STORAGE = 'flask_collect.storage.link'
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
    OAUTH_CREDENTIALS = {
        'twitter': {
            'id': '3RzWQclolxWZIMq5LJqzRZPTl',
            'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
        },
        'linkedin': {
            'id': '77nqaknch3hzpa',
            'secret': 'J8rjhnxqCx4IeqOO'
        }
    }
