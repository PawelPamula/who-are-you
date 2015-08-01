"""Init Extension."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def setup_app(app):
    """Init the extension with app context."""
    db.init_app(app)
    return app
