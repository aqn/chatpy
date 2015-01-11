# Chatpy
# Copyright 2013-2015 aqn
# the original source code is written by Joshua Roesslein (Tweepy)
# See LICENSE for details.
import six


def import_simplejson():
    try:
        import simplejson as json
    except ImportError:
        try:
            import json  # Python 2.6+
        except ImportError:
            try:
                from django.utils import simplejson as json  # Google App Engine
            except ImportError:
                raise ImportError("Can't load a json library")

    return json


def convert_to_utf8_str(arg):
    if isinstance(arg, six.text_type):
        return arg
    arg = six.text_type(arg).encode('utf-8')
    return arg