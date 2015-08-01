"""Create the app."""
import os
import sys

from flask import Flask, render_template

from flask_registry import (
    BlueprintAutoDiscoveryRegistry,
    ConfigurationRegistry,
    ExtensionRegistry,
    PackageRegistry,
    Registry
)


def create_app(instance_path="", env="prod"):
    """Create the app."""
    app_name = '.'.join(__name__.split('.')[0:2])

    instance_path = instance_path or os.path.join(
        sys.prefix, 'var', app_name + '-instance'
    )
    try:
        if not os.path.exists(instance_path):
            os.makedirs(instance_path)
    except Exception:
        pass

    app = Flask(
        app_name,
        instance_path=instance_path,
        instance_relative_config=True,
        static_folder=os.path.join(instance_path, 'static'),
    )

    app.config['ENV'] = env
    env_object = "webfest.base.config.{0}Config".format(
        env.capitalize()
    )
    app.config.from_object(env_object)
    app.config.from_envvar('webfest_ENV_SRC', silent=True)
    app.config.from_pyfile('application.cfg', silent=True)

    # Ignore slashes
    app.url_map.strict_slashes = False

    # Add the proxies
    Registry(app=app)
    app.extensions['registry'].update(
        packages=PackageRegistry(app)
    )
    app.extensions['registry'].update(
        extensions=ExtensionRegistry(app),
        blueprints=BlueprintAutoDiscoveryRegistry(app=app),
    )
    ConfigurationRegistry(app)
    _setup_app_errors(app)
    return app


def _setup_app_errors(app):
    """Setup errors."""
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('error/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('error/500.html'), 500
