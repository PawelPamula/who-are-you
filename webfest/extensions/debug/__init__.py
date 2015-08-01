"""Init Extension."""

from flask_debugtoolbar import DebugToolbarExtension

debug = DebugToolbarExtension()


def setup_app(app):
    """Init the extension with app context."""
    debug.init_app(app)
    return app
