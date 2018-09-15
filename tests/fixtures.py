import pytest


@pytest.fixture()
def conf_request():
    class Request(object):
        def __init__(self, post):
            self.POST = post

    return Request
