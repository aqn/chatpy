# Chatpy
# Copyright 2013-2015 aqn
# the original source code is written by Joshua Roesslein (Tweepy)
# See LICENSE for details.

import six


class ChatpyError(Exception):
    """Chatpy exception"""

    def __init__(self, reason, response=None):
        self.reason = six.text_type(reason)
        self.response = response
        Exception.__init__(self, reason)

    def __str__(self):
        return self.reason

