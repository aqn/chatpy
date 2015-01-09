# Chatpy
# Copyright 2013-2015 aqn
# See LICENSE for details.


class ChatpyError(Exception):
    """Chatpy exception"""

    def __init__(self, reason, response=None):
        self.reason = unicode(reason)
        self.response = response
        Exception.__init__(self, reason)

    def __str__(self):
        return self.reason

