"""Init Extension."""

from flask_assets import Environment
from flask_registry import ModuleAutoDiscoveryRegistry, RegistryProxy

assets = Environment()


class BundlesAutoDiscoveryRegistry(ModuleAutoDiscoveryRegistry):

    """Registry that searches for bundles.

    Its registry is a list of the package name and the bundle itself. This way
    you can keep track of where a bundle was loaded from.
    """

    def __init__(self, module_name=None, app=None, with_setup=False,
                 silent=False):
        """Initialize the bundle auto discovery registry.

        :param module_name: where to look for bundles (default: bundles)
        :type module_name: str
        """
        super(BundlesAutoDiscoveryRegistry, self).__init__(
            module_name or 'bundles', app=app, with_setup=with_setup,
            silent=silent)

bundles = RegistryProxy("bundles", BundlesAutoDiscoveryRegistry)


def setup_app(app):
    """Init the extension with app context."""
    assets.init_app(app)
    return app
