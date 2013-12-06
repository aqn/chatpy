from config import chatwork_token

from chatpy.api import API
from chatpy.auth import TokenAuthHandler
from chatpy.error import ChatpyError

from nose.tools import raises


def test_auth_ok():
    auth = TokenAuthHandler(chatwork_token)
    api = API(auth)
    api.me()


@raises(ChatpyError)
def test_auth_ng():
    auth = TokenAuthHandler("invalid_token")
    api = API(auth)
    api.me()
