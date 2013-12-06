# Chatpy
# Copyright 2013 aqn
# See LICENSE for details.

from chatpy.binder import bind_api
from chatpy.parsers import ModelParser


class API(object):
    """Twitter API"""

    def __init__(self, auth_handler=None,
                 host='api.chatwork.com',
                 cache=None, secure=True, api_root='/v1',
                 retry_count=0, retry_delay=0, retry_errors=None, timeout=60,
                 parser=None, compression=False):
        self.auth = auth_handler
        self.host = host
        self.api_root = api_root
        self.cache = cache
        self.secure = secure
        self.compression = compression
        self.retry_count = retry_count
        self.retry_delay = retry_delay
        self.retry_errors = retry_errors
        self.timeout = timeout
        self.parser = parser or ModelParser()

    """ GET /me """
    me = bind_api(
        path='/me',
        payload_type='account'
    )

    """ GET /my/status """
    status = bind_api(
        path='/my/status',
        payload_type='status'
    )

    """ GET /my/tasks """
    tasks = bind_api(
        path='/my/tasks',
        payload_type='task', payload_list=True,
    )

    """ GET /rooms """
    rooms = bind_api(
        path='/rooms',
        payload_type='room', payload_list=True,
    )

    """ GET /rooms/{room_id} """
    get_room = bind_api(
        path='/rooms/{room_id}',
        payload_type='room',
        allowed_param=['room_id']
    )

    """ POST /rooms/{room_id}/messages """
    post_message = bind_api(
        path='/rooms/{room_id}/messages',
        method='POST',
        allowed_param=['room_id', 'body']
    )

