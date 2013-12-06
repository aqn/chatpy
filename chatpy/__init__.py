# chatpy
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.

"""
Chatwork API library
"""
__version__ = '0.1'
__author__ = 'aqn'
__license__ = 'MIT'

from chatpy.models import Status, User, DirectMessage, Friendship, SavedSearch, SearchResults, ModelFactory, Category
from chatpy.error import TweepError
from chatpy.api import API
from chatpy.cache import Cache, MemoryCache, FileCache
from chatpy.auth import TokenAuthHandler

# Global, unauthenticated instance of API
api = API()


def debug(level=1):

    import httplib
    httplib.HTTPConnection.debuglevel = level

