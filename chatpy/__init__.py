# chatpy
# Copyright 2013-2015 aqn
# See LICENSE for details.

"""
Chatwork API library
"""
__version__ = '0.2.0'
__license__ = 'MIT'

from chatpy.models import Status, ModelFactory
from chatpy.error import ChatpyError
from chatpy.api import API
from chatpy.cache import Cache, MemoryCache, FileCache
from chatpy.auth import TokenAuthHandler

# Global, unauthenticated instance of API
api = API()


def debug(level=1):

    import httplib
    httplib.HTTPConnection.debuglevel = level

