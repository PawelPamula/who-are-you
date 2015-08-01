"""Init the app bundles."""
from flask_assets import Bundle

js = Bundle(
    "vendors/jquery/dist/jquery.js",
    "vendors/bootstrap/dist/js/bootstrap.js",
    filters='jsmin',
    output='main.js'
)
