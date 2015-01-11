# Chatpy
# Copyright 2013-2015 aqn
# the original source code is written by Joshua Roesslein (Tweepy)
# See LICENSE for details.


from chatpy.error import ChatpyError
from chatpy.api import API


class AuthHandler(object):

    def apply_auth(self, url, method, headers, parameters):
        """Apply authentication headers to request"""
        raise NotImplementedError

    def get_username(self):
        """Return the username of the authenticated user"""
        raise NotImplementedError


class TokenAuthHandler(AuthHandler):

    def __init__(self, token):
        self.token = token
        self.username = None

    def apply_auth(self, url, method, headers, parameters):
        headers['X-ChatWorkToken'] = self.token

    def get_username(self):
        if self.username is None:
            api = API(self)
            user = api.me()
            if user:
                self.username = user.name
            else:
                raise ChatpyError("Unable to get username, invalid token!")
        return self.username
