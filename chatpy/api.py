# Chatpy
# Copyright 2013-2015 aqn
# the original source code is written by Joshua Roesslein (Tweepy)
# See LICENSE for details.

from chatpy.binder import bind_api
from chatpy.parsers import ModelParser


class API(object):
    """Chatwork API"""

    def __init__(self, auth_handler=None,
                 host='api.chatwork.com',
                 cache=None, secure=True, api_root='/v2',
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
        payload_type='my_account'
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

    """ GET /contacts """
    contacts = bind_api(
        path='/contacts',
        payload_type='account',
        payload_list=True
    )

    """ GET /rooms """
    rooms = bind_api(
        path='/rooms',
        payload_type='room', payload_list=True,
    )

    """ POST /rooms """
    create_room = bind_api(
        path='/rooms',
        method='POST',
        allowed_param=['description', 'icon_preset', 'members_admin_ids', 'members_member_ids', 'members_readonly_ids',
                       'name']
    )

    """ GET /rooms/{room_id} """
    get_room = bind_api(
        path='/rooms/{room_id}',
        payload_type='room',
        allowed_param=['room_id']
    )

    """ PUT /rooms/{room_id} """
    change_room = bind_api(
        path='/rooms/{room_id}',
        method='PUT',
        allowed_param=['description', 'icon_preset', 'name']
    )

    """ DELETE/rooms/{room_id} """
    delete_room = bind_api(
        path='/rooms/{room_id}',
        method='DELETE',
        allowed_param=["room_id", "action_type"]
    )

    """ GET /rooms/{room_id}/members """
    get_members = bind_api(
        path='/rooms/{room_id}/members',
        payload_type='account',
        payload_list=True,
        allowed_param=['room_id']
    )
    """ PUT /rooms/{room_id}/members """
    change_room_members = bind_api(
        path='/rooms/{room_id}/members',
        method='PUT',
        allowed_param=['members_admin_ids', 'members_member_ids', 'members_readonly_ids']
    )

    """ GET /rooms/{room_id}/messages """
    messages = bind_api(
        path='/rooms/{room_id}/messages',
        method='GET',
        allowed_param=['force'],
        payload_type='message',
        payload_list=True
    )

    """ POST /rooms/{room_id}/messages """
    post_message = bind_api(
        path='/rooms/{room_id}/messages',
        method='POST',
        allowed_param=['room_id', 'body']
    )

    """ GET /rooms/{room_id}/tasks """
    room_tasks = bind_api(
        path='/rooms/{room_id}/tasks',
        payload_type='task',
        payload_list=True,
        allowed_param=['room_id']
    )

    """ POST /rooms/{room_id}/tasks """
    post_tasks = bind_api(
        path='/rooms/{room_id}/tasks',
        method='POST',
        payload_type='task',
        allowed_param=['room_id', 'body', 'to_ids', 'limit']
    )

    """ GET /rooms/{room_id}/tasks/{task_id} """
    get_task = bind_api(
        path='/rooms/{room_id}/tasks/{task_id}',
        payload_type='task',
        allowed_param=['room_id', 'task_id']
    )
    """ GET /rooms/{room_id}/files """
    files = bind_api(
        path='/rooms/{room_id}/files',
        payload_type='attachment',
        payload_list=True,
        allowed_param=['room_id']
    )

    """ GET /rooms/{room_id}/files/{file_id} """
    get_file = bind_api(
        path='/rooms/{room_id}/files/{file_id}',
        payload_type='attachment',
        allowed_param=['room_id', 'file_id']
    )
