"""Init Extension."""

from flask_cache import Cache

cache = Cache()


def setup_app(app):
    """Init the extension with app context."""
    cache.init_app(app)
    return app
