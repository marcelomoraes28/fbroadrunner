import pytest

from fbroadrunner.exceptions import FbRoadRunnerFieldError
from fbroadrunner.pyramid import fb_messenger, fb_publication


@fb_messenger(app_id=12345678, link='https://fbrunner.com',
              redirect_uri='https://fbrunner.com')
def example_fb_messenger(request, **kwargs):
    return kwargs['fb_url']


@fb_messenger(link='https://fbrunner.com', redirect_uri='https://fbrunner.com')
def example_fb_messenger_without_app_id(request, **kwargs):
    return kwargs['fb_url']


@fb_messenger(app_id=12345678)
def example_fb_messenger_without_parameters(request, **kwargs):
    return kwargs['fb_url']


@fb_publication(app_id=12345678, link='https://fbrunner.com',
                redirect_uri='https://fbrunner.com')
def example_fb_publication(request, **kwargs):
    return kwargs['fb_url']


@fb_publication(link='https://fbrunner.com',
                redirect_uri='https://fbrunner.com')
def example_fb_publication_without_app_id(request, **kwargs):
    return kwargs['fb_url']


@fb_publication(app_id=12345678)
def example_fb_publication_without_parameters(request, **kwargs):
    return kwargs['fb_url']


def test_fb_publication_basic(mocker, conf_request):
    request = conf_request(post={})
    fb_pub = example_fb_publication(request=request)
    assert fb_pub == 'https://www.facebook.com/dialog/feed?app_id=12345678&link=https%3A%2F%2Ffbrunner.com&redirect_uri=https%3A%2F%2Ffbrunner.com'


def test_fb_publication_with_one_parameter_with_post(mocker, conf_request):
    request = conf_request(post={"fb_redirect_uri": "http://road.com"})
    fb_pub = example_fb_publication(request=request)
    assert fb_pub == 'https://www.facebook.com/dialog/feed?app_id=12345678&link=https%3A%2F%2Ffbrunner.com&redirect_uri=https%3A%2F%2Ffbrunner.com'


def test_fb_publication_raises(mocker, conf_request):
    request = conf_request(post={"fb_link": "http://road.com",
                                 "fb_redirect_uri": "http://road.com"})
    with pytest.raises(FbRoadRunnerFieldError):
        example_fb_publication_without_app_id(request=request)


def test_fb_publication_with_env(monkeypatch, conf_request):
    monkeypatch.setenv('FB_APP_ID', 123456789)
    request = conf_request(post={})
    fb_pub = example_fb_publication_without_app_id(request=request)
    assert fb_pub == 'https://www.facebook.com/dialog/feed?app_id=123456789&link=https%3A%2F%2Ffbrunner.com&redirect_uri=https%3A%2F%2Ffbrunner.com'


def test_example_fb_publication_with_all_parameters_with_post(conf_request):
    request = conf_request(
        post={"fb_redirect_uri": "http://road.com",
              "display": "popup&amp;caption=An%20example%20caption",
              "to": "1234", "from": "7575", "source": "12345",
              "link": "https://roadrunner.com"})
    fb_pub = example_fb_publication_without_parameters(request=request)
    assert fb_pub == 'https://www.facebook.com/dialog/feed?display=popup%26amp%3Bcaption%3DAn%2520example%2520caption&to=1234&from=7575&source=12345&link=https%3A%2F%2Froadrunner.com&app_id=12345678'


def test_fb_messenger_basic(conf_request):
    request = conf_request(post={})
    fb_message = example_fb_messenger(request=request)
    assert fb_message == 'http://www.facebook.com/dialog/send?app_id=12345678&redirect_uri=https%3A%2F%2Ffbrunner.com&link=https%3A%2F%2Ffbrunner.com'


def test_fb_messenger_with_one_parameter_with_post(conf_request):
    request = conf_request(post={"fb_redirect_uri": "http://road.com"})
    fb_message = example_fb_messenger(request=request)
    assert fb_message == 'http://www.facebook.com/dialog/send?app_id=12345678&redirect_uri=https%3A%2F%2Ffbrunner.com&link=https%3A%2F%2Ffbrunner.com'


def test_fb_messenger_raises(conf_request):
    request = conf_request(post={"fb_link": "http://road.com",
                                 "fb_redirect_uri": "http://road.com"})
    with pytest.raises(FbRoadRunnerFieldError):
        example_fb_messenger_without_app_id(request=request)


def test_fb_messenger_with_env(monkeypatch, conf_request):
    monkeypatch.setenv('FB_APP_ID', 123456789)
    request = conf_request(post={})
    fb_message = example_fb_messenger_without_app_id(request=request)
    assert fb_message == 'http://www.facebook.com/dialog/send?app_id=123456789&redirect_uri=https%3A%2F%2Ffbrunner.com&link=https%3A%2F%2Ffbrunner.com'


def test_example_fb_messenger_with_all_parameters_with_post(conf_request):
    request = conf_request(
        post={"fb_redirect_uri": "http://road.com",
              "display": "popup&amp;caption=An%20example%20caption",
              "to": "1234", "link": "https://roadrunner.com"})
    fb_message = example_fb_messenger_without_parameters(request=request)
    assert fb_message == 'http://www.facebook.com/dialog/send?display=popup%26amp%3Bcaption%3DAn%2520example%2520caption&to=1234&link=https%3A%2F%2Froadrunner.com&app_id=12345678'
