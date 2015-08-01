"""Base pages Blueprint."""

from flask import (
    Blueprint, render_template, url_for, redirect, flash,
    session, request, jsonify
)
from flask_login import logout_user, login_user, current_user
from webfest.modules.linkedin import linkedin

blueprint = Blueprint(
    'base', __name__, template_folder='templates', static_folder='static'
)


@blueprint.route('/')
def index():
    return render_template('home.html')


@blueprint.route('/data')
def data():
    if 'linkedin_token' in session:
        me = linkedin.get('people/~')
        return jsonify(me.data)
    return redirect(url_for('base.login'))


@blueprint.route('/login')
def login():
    return linkedin.authorize(callback=url_for('base.authorized', _external=True))


@blueprint.route('/logout')
def logout():
    session.pop('linkedin_token', None)
    return redirect(url_for('base.index'))


@blueprint.route('/login/authorized')
def authorized():
    resp = linkedin.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['linkedin_token'] = (resp['access_token'], '')
    return redirect(url_for('base.data'))
