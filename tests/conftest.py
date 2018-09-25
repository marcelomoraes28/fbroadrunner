import pytest


@pytest.fixture(scope="module")
def conf_request():
    class Request(object):
        def __init__(self, post):
            self.POST = post

    return Request


@pytest.fixture(scope="class")
def message_payload():
    return {
        "default_link": "http://fbroadrunner",
        "default_display": "display:none",
        "default_redirect_uri": "http://fbroadrunner",
        "default_to": "fbroadrunner",
    }


@pytest.fixture(scope="class")
def publication_payload():
    return {
        "default_link": "http://fbroadrunner",
        "default_display": "display:none",
        "default_redirect_uri": "http://fbroadrunner",
        "default_to": "fbroadrunner",
        "default_from": "alien",
        "default_source": "predator"
    }
