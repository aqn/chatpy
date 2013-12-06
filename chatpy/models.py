# Chatpy
# Copyright 2013 aqn
# See LICENSE for details.

import datetime


class ResultSet(list):
    """A list like object that holds results from a Chatwork API query."""
    def __init__(self, max_id=None, since_id=None):
        super(ResultSet, self).__init__()
        self._max_id = max_id
        self._since_id = since_id

    @property
    def max_id(self):
        if self._max_id:
            return self._max_id
        ids = self.ids()
        return max(ids) if ids else None

    @property
    def since_id(self):
        if self._since_id:
            return self._since_id
        ids = self.ids()
        return min(ids) if ids else None

    def ids(self):
        return [item.id for item in self if hasattr(item, 'id')]


class Model(object):

    def __init__(self, api=None):
        self._api = api

    def __getstate__(self):
        # pickle
        pickle = dict(self.__dict__)
        try:
            del pickle['_api']  # do not pickle the API reference
        except KeyError:
            pass
        return pickle

    @classmethod
    def parse(cls, api, json):
        """Parse a JSON object into a model instance."""
        raise NotImplementedError

    @classmethod
    def parse_list(cls, api, json_list):
        """Parse a list of JSON objects into a result set of model instances."""
        results = ResultSet()
        for obj in json_list:
            if obj:
                results.append(cls.parse(api, obj))
        return results


class Account(Model):

    @classmethod
    def parse(cls, api, json):
        account = cls(api)
        for k, v in json.items():

            setattr(account, k, v)
        return account


class Task(Model):

    @classmethod
    def parse(cls, api, json):
        task = cls(api)

        for k, v in json.items():
            if k in ('assigned_by_account', 'account'):
                account_model = getattr(api.parser.model_factory, 'account')
                account = account_model.parse(api, v)
                setattr(task, k,  account)
            elif k == 'limit_time':
                utc_time = datetime.datetime.utcfromtimestamp(v)
                setattr(task, k, utc_time)
            else:
                setattr(task, k, v)
        return task


class Room(Model):

    @classmethod
    def parse(cls, api, json):
        room = cls(api)

        for k, v in json.items():
            if k == 'last_update_time':
                utc_time = datetime.datetime.utcfromtimestamp(v)
                setattr(room, k, utc_time)
            else:
                setattr(room, k, v)
        return room

    def post_message(self, **kwargs):
        return self._api.post_message(room_id=self.room_id, **kwargs)


class File(Model):

    @classmethod
    def parse(cls, api, json):
        f = cls(api)

        for k, v in json.items():

            if k == 'account':
                account_model = getattr(api.parser.model_factory, 'account')
                account = account_model.parse(api, v)
                setattr(f, k,  account)
            elif k == 'upload_time':
                utc_time = datetime.datetime.utcfromtimestamp(v)
                setattr(f, k, utc_time)
            else:
                setattr(f, k, v)

        return f


class Message(Model):

    @classmethod
    def parse(cls, api, json):
        message = cls(api)

        for k, v in json.items():
            setattr(message, k, v)

        return message


class Status(Model):

    @classmethod
    def parse(cls, api, json):
        status = cls(api)

        for k, v in json.items():
            setattr(status, k, v)

        return status


class JSONModel(Model):

    @classmethod
    def parse(cls, api, json):
        return json


class IDModel(Model):

    @classmethod
    def parse(cls, api, json):
        if isinstance(json, list):
            return json
        else:
            return json['ids']


class ModelFactory(object):
    """
    Used by parsers for creating instances
    of models. You may subclass this factory
    to add your own extended models.
    """

    room = Room
    account = Account
    task = Task
    status = Status
    message = Message
    attachment = File

    json = JSONModel
    ids = IDModel

