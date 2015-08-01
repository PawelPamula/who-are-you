from flask_oauthlib.client import OAuth
oauth = OAuth()

def setup_app(app):
    """Init oauth."""
    oauth.init_app(app)
    return app
