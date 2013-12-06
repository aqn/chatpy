*******************************
Chatpy: Chatwork API for Python
*******************************

.. image:: https://travis-ci.org/aqn/chatpy.png?branch=master
    :target: https://travis-ci.org/aqn/chatpy

Chatpy is a `Chatwork API`_ Library which strongly inspired by Tweepy_.

==============
Supported API
==============

- Endpoint: /me
    - GET /me
- Endpoint: /my
    - GET /my/status
    - GET /my/tasks
- Endpoint: contacts
    - GET /contacts (not implemented)
- Endpoint: /rooms
    - GET /rooms
    - POST /rooms (not implemented)
    - GET /rooms/{room_id}
    - PUT /rooms/{room_id} (not implemented)
    - DELETE/rooms/{room_id} (not implemented)
    - GET /rooms/{room_id}/members (not implemented)
    - PUT /rooms/{room_id}/members (not implemented)
    - GET /rooms/{room_id}/messages (upstream not implemented)
    - POST /rooms/{room_id}/messages
    - GET /rooms/{room_id}/tasks (not implemented)
    - POST /rooms/{room_id}/tasks (not implemented)
    - GET /rooms/{room_id}/tasks/{task_id} (not implemented)
    - POST /rooms/{room_id}/tasks/{task_id} (not implemented)
    - GET /rooms/{room_id}/files (not implemented)
    - GET /rooms/{room_id}/files/{file_id} (not implemented)


.. _Chatwork API: http://developer.chatwork.com/ja/index.html
.. _Tweepy: https://github.com/tweepy/tweepy
