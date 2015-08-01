"""Init Extension."""

from flask_restful import Api


def setup_app(app):
    """Init the extension with app context."""
    api = Api(app=app)
    app.extensions['restful'] = api
    return app
