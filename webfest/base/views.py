"""Base pages Blueprint."""

from flask import (
    Blueprint, render_template, url_for, request, redirect
)

blueprint = Blueprint(
    'base', __name__, template_folder='templates', static_folder='static'
)


@blueprint.route('/')
def index():
    """Index page."""
    return render_template('home.html')
