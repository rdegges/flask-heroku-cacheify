from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'Flask-Heroku-Cacheify',
    version = '1.5',
    py_modules = ('flask_cacheify', ),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = [
        'Flask-Cache>=0.11.1',
        'pylibmc>=1.2.3',
        'redis>=2.7.2'
    ],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'rdegges@gmail.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/flask-heroku-cacheify',
    keywords = 'flask heroku cloud cache memcache memcached redis awesome',
    description = 'Automatic Flask cache configuration on Heroku.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)
