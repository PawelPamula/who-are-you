"""The Heroku setup."""

import os

from .factory import create_app

instance_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 'instance'
)

app = create_app(instance_path=instance_path, env="Heroku")
