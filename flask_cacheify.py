from os import environ
from types import NoneType

from flask.ext.cache import Cache


class Cacheify(object):
    """This class is used to auto-configure an appropriate cache for your Flask
    application.
    """
    def __init__(self, app=None, config=None):
        self.app = app
        self.config = config

        if app is not None:
            self.init_app(app, config)

    def init_app(self, app, config=None):
        """Initialize an appropriate cache for your Flask application."""
        if not isinstance(config, (NoneType, dict)):
            raise ValueError('ERROR: config must be an instance of dict or '
                    'NoneType.')

        if config is None:
            config = self.config

        if config is None:
            config = app.config

        self.set_preferred(self.get_addons(), config)

        if not hasattr(app, 'extensions'):
            app.extensions = {}

        app.extensions.setdefault('cache', {})
        app.extensions['cacheify'][self] = Cache(app, config)

    def get_addons(self):
        """Scan for environment variables that allow us to hook up to
        Flask-Cache.

        Currently, we support:

            - MemCachier (https://addons.heroku.com/memcachier)
        """
        addons = {}

        # Look for MemCachier.
        if any([k.startswith('MEMCACHIER_') for k in environ]):
            addons['memcachier'] = {
                'servers': [environ.get('MEMCACHIER_SERVERS')],
                'username': environ.get('MEMCACHIER_USERNAME'),
                'password': environ.get('MEMCACHIER_PASSWORD'),
            }
        else:
            addons['memcachier'] = None

        return addons

    def set_preferred(self, addons, config):
        """Given a dictionary of available addons, pick the preferred addon to
        use.

        We'll try to use whichever is the "best" provider, based on the
        environment variables available to us.
        """
        if addons['memcachier']:
            config.setdefault('CACHE_TYPE', 'saslmemcached')
            config.setdefault('CACHE_MEMCACHED_SERVERS',
                    addons['memcachier']['servers'])
            config.setdefault('CACHE_MEMCACHED_USERNAME',
                    addons['memcachier']['username'])
            config.setdefault('CACHE_MEMCACHED_PASSWORD',
                    addons['memcachier']['password'])
