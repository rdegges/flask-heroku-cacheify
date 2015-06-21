# flask-heroku-cacheify

Automatic Flask cache configuration on Heroku.

![Thinking Man Sketch](https://raw.github.com/rdegges/flask-heroku-cacheify/master/assets/thinking-man-sketch.jpg)


## Purpose

Configuring your cache on Heroku can be a time sink.  There are lots of
different caching addons available on Heroku (Redis, Memcached, etc.), and among
those -- lots of competitors.

`flask-heroku-cacheify` makes your life easy by automatically configuring your
Flask application to work with whatever caching addons you've got provisioned
on Heroku, allowing you to easily swap out addon providers at will, without any
trouble.  And, just in case you don't have any suitable Heroku addons available,
`flask-heroku-cacheify` will default back to using local memory for your cache!

Instead of looking through documentation, testing stuff out, etc.,
`flask-heroku-cacheify` will just do everything for you :)


## Install

To install `flask-heroku-cacheify`, use [pip](http://pip.readthedocs.org/en/latest/).

```bash
$ pip install flask-heroku-cacheify
```

**NOTE**: If you're install `flask-heroku-cacheify` locally, you'll need to
have `libmemcached-dev` installed on your OS (with SASL support).

Next, modify your `requirements.txt` file in your home directory, and add the
following to the bottom of your file:

```bash
Flask-Heroku-Cacheify>=1.3
pylibmc>=1.2.3
```

The above will ensure that Heroku pulls in the required C header files (in case
you decide to use memcached).  This step is **required**.


## Pick an Addon

Heroku has lots of available addons you can use for caching.
`flask-heroku-cacheify` currently works with them all!  That means no matter
which option you choose, your cache will work out of the box, guaranteed!

Below is a list of the addons you can install to get started, you should have at
least one of these activated on your Heroku app -- otherwise, your cache will be
in 'local memory' only, and won't be very useful.

- [MemCachier](https://addons.heroku.com/memcachier)
- [RedisGreen](https://addons.heroku.com/redisgreen)
- [Redis Cloud](https://addons.heroku.com/rediscloud)
- [Redis To Go](https://addons.heroku.com/redistogo)
- [openredis](https://addons.heroku.com/openredis)

**NOTE** My favorite providers are MemCachier (for memcache), and openredis for
redis.  Both are equally awesome as cache providers.  If you're in need of a
stable cache provider for large applications, I'd recommend
[RedisGreen](https://addons.heroku.com/redisgreen) -- they use dedicated EC2
instances (which greatly improves your server power) and have an excellent
interface.


## Usage

Using `flask-heroku-cacheify` is *super easy*!  In your `app.py` (or wherever
you define your Flask application), add the following:

```python
from flask.ext.cacheify import init_cacheify

app = Flask(__name__)
cache = init_cacheify(app)
```

Once you've got your `cache` global defined, you can use it anywhere in your
Flask app:

```python
>>> from app import cache
>>> cache.set('hi', 'there', 30)
>>> cache.get('hi')
'there'
```

How does this work?  In the background, `flask-heroku-cacheify` is really just
automatically configuring the popular
[Flask-Cache](http://pythonhosted.org/Flask-Cache/) extension!  This means, you
can basically skip down to [this
part](http://pythonhosted.org/Flask-Cache/#caching-view-functions) of their
documentation, and begin using all the methods listed there, without worrying
about setting up your caches!  Neat, right?

For more information and examples of how to use your cache, don't forget to read
the [Flask-Cache](http://pythonhosted.org/Flask-Cache/) documentation.


## Like This?

Like this software?  If you really enjoy `flask-heroku-cacheify`, you can show
your appreciation by:

- Sending me some bitcoin, my address is: **17BE6Q6fRgxJutnn8NsQgeKnACFjzWLbQT**
- Tipping me on [gittip](https://www.gittip.com/rdegges/).

Either way, thanks!  <3


## Changelog

v1.5: 06-20-2015

    - Removing MyRedis addon support -- the addon has been shut down.

v1.4: 04-04-2015

    - Fixing typos in README.
    - Adding Python 3 compatibility.

v1.3: 05-31-2012

    - Fixing bug with memcachier support (thanks @eriktaubeneck)!

v1.2: 04-18-2013

    - Adding proper documentation.

v1.1: 04-18-2013

    - Adding support for MyRedis.
    - Adding support for Redis Cloud.
    - Adding support for Redis To Go.
    - Adding support for openredis.

v1.0: 04-18-2013

    - Fixing bug with RedisGreen support.

v0.9: 04-18-2013

    - First *real* release! Supports MemCachier and RedisGreen!

v0.8: 04-18-2013

    - Pushing eigth release to PyPI (don't use this still!).

v0.7: 04-18-2013

    - Pushing seventh release to PyPI (don't use this still!).

v0.6: 04-18-2013

    - Pushing sixth release to PyPI (don't use this still!).

v0.5: 04-18-2013

    - Pushing fifth release to PyPI (don't use this still!).

v0.4: 04-18-2013

    - Pushing fourth release to PyPI (don't use this still!).

v0.3: 04-18-2013

    - Pushing third release to PyPI (don't use this still!).

v0.2: 04-18-2013

    - Pushing second release to PyPI (don't use this still!).

v0.1: 04-18-2013

    - Pushing first release to PyPI (don't use this yet!).

v0.0: 04-14-2013

    - Started work >:)
