# chatpy
# Copyright 2013-2015 aqn
# the original source code is written by Joshua Roesslein (Tweepy)
# See LICENSE for details.

"""
Chatwork API library
"""
__version__ = '0.3.0'
__license__ = 'MIT'

from chatpy.models import Status, ModelFactory
from chatpy.error import ChatpyError
from chatpy.api import API
from chatpy.cache import Cache, MemoryCache, FileCache
from chatpy.auth import TokenAuthHandler

# Global, unauthenticated instance of API
api = API()


def debug(level=1):
    from six.moves import http_client
    http_client.HTTPConnection.debuglevel = level

