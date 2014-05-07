*******************************
Chatpy: Chatwork API for Python
*******************************

.. image:: https://travis-ci.org/aqn/chatpy.png?branch=master
    :target: https://travis-ci.org/aqn/chatpy

Chatpy is a `Chatwork API`_ Library which strongly inspired by Tweepy_.

=============
Installation
=============

::

    $ pip install git+https://github.com/aqn/chatpy.git


=============
Supported API
=============

- Endpoint: /me
    - GET /me
- Endpoint: /my
    - GET /my/status
    - GET /my/tasks
- Endpoint: contacts
    - GET /contacts
- Endpoint: /rooms
    - GET /rooms
    - POST /rooms (not implemented)
    - GET /rooms/{room_id}
    - PUT /rooms/{room_id} (not implemented)
    - DELETE/rooms/{room_id} (not implemented)
    - GET /rooms/{room_id}/members
    - PUT /rooms/{room_id}/members (not implemented)
    - GET /rooms/{room_id}/messages (upstream not implemented)
    - POST /rooms/{room_id}/messages
    - GET /rooms/{room_id}/tasks
    - POST /rooms/{room_id}/tasks (not implemented)
    - GET /rooms/{room_id}/tasks/{task_id}
    - GET /rooms/{room_id}/files
    - GET /rooms/{room_id}/files/{file_id}


.. _Chatwork API: http://developer.chatwork.com/ja/index.html
.. _Tweepy: https://github.com/tweepy/tweepy
