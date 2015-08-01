"""User models."""

from webfest.extensions.sqlalchemy import db
from flask_login import UserMixin


class User(UserMixin, db.Model):

    """Define the user model."""

    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
