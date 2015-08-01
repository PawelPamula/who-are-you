"""Init Extension."""

from flask import g
from flask_login import LoginManager, current_user

login_manager = LoginManager()


def setup_app(app):
    """Init the extension with app context."""
    from webfest.modules.user.models import User

    login_manager.login_view = "index"
    login_manager.login_message_category = "warning"

    @login_manager.user_loader
    def load_user(uid):
        """Load user with id."""
        return User.query.get(int(uid))

    @app.before_request
    def before_request():
        g.user = current_user

    login_manager.init_app(app)
    return app
