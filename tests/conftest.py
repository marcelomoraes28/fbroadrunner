import pytest


@pytest.fixture(scope="module")
def conf_request():
    class Request(object):
        def __init__(self, post):
            self.POST = post

    return Request


@pytest.fixture(scope="module")
def message_payload():
    return {
        "app_id": "12345",
        "default_link": "http://fbroadrunner",
        "default_display": "display:none",
        "default_redirect_uri": "http://fbroadrunner",
        "default_to": "fbroadrunner",
    }
