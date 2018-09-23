from urllib import parse
from fbroadrunner.functions import get_publication_url, get_message_url, \
    get_app_id_from_env


def test_get_message_url(message_payload, monkeypatch):
    is_mobile = False
    payload = message_payload
    test_1 = get_message_url(post=payload, app_id=12345, link=None,
                             display=None, to=None, redirect_uri=None,
                             mobile=is_mobile)
    parsed = parse.urlparse(test_1)
    qs = parse.parse_qs(parsed.query)
    assert "app_id" in qs
    assert qs["app_id"][0] == "12345"
    assert "link" in qs
    assert qs["link"][0] == "http://fbroadrunner"
    assert "redirect_uri" in qs
    assert qs["redirect_uri"][0] == "http://fbroadrunner"
    assert "to" in qs
    assert qs["to"][0] == "fbroadrunner"

    monkeypatch.setenv('FB_APP_ID', 5555)
    test_2 = get_message_url(post=payload, app_id=None, link=None,
                             display=None, to=None, redirect_uri=None,
                             mobile=is_mobile)
    parsed = parse.urlparse(test_2)
    qs = parse.parse_qs(parsed.query)
    assert "app_id" in qs
    assert qs["app_id"][0] == "5555"

    del payload["default_link"]
    test_3 = get_message_url(post=payload, app_id=None,
                             link="https://localhost",
                             display=None, to=None, redirect_uri=None,
                             mobile=is_mobile)
    parsed = parse.urlparse(test_3)
    qs = parse.parse_qs(parsed.query)
    assert "redirect_uri" in qs
    assert qs["link"][0] == "https://localhost"

    del payload["default_redirect_uri"]
    test_4 = get_message_url(post=payload, app_id=None,
                             link="https://localhost",
                             display=None, to=None, redirect_uri="127.0.0.1",
                             mobile=is_mobile)
    parsed = parse.urlparse(test_4)
    qs = parse.parse_qs(parsed.query)
    assert "redirect_uri" in qs
    assert qs["redirect_uri"][0] == "127.0.0.1"

    del payload["default_to"]

    test_5 = get_message_url(post=payload, app_id=None,
                             link="https://localhost",
                             display=None, to='predator',
                             redirect_uri="127.0.0.1",
                             mobile=is_mobile)
    parsed = parse.urlparse(test_5)
    qs = parse.parse_qs(parsed.query)
    assert "to" in qs
    assert qs["to"][0] == "predator"


def test_get_message_url_mobile(message_payload, monkeypatch):
    is_mobile = True
    payload = message_payload
    test_1 = get_message_url(post=payload, app_id=12345, link=None,
                             display=None, to=None, redirect_uri=None,
                             mobile=is_mobile)
    parsed = parse.urlparse(test_1)
    qs = parse.parse_qs(parsed.query)
    assert "app_id" in qs
    assert qs["app_id"][0] == "12345"
    assert "link" in qs
    assert qs["link"][0] == "http://fbroadrunner"
    assert "redirect_uri" in qs
    assert qs["redirect_uri"][0] == "http://fbroadrunner"
    assert "to" in qs
    assert qs["to"][0] == "fbroadrunner"

    monkeypatch.setenv('FB_APP_ID', 5555)
    test_2 = get_message_url(post=payload, app_id=None, link=None,
                             display=None, to=None, redirect_uri=None,
                             mobile=is_mobile)
    parsed = parse.urlparse(test_2)
    qs = parse.parse_qs(parsed.query)
    assert "app_id" in qs
    assert qs["app_id"][0] == "5555"

    del payload["default_link"]
    test_3 = get_message_url(post=payload, app_id=None,
                             link="https://localhost",
                             display=None, to=None, redirect_uri=None,
                             mobile=is_mobile)
    parsed = parse.urlparse(test_3)
    qs = parse.parse_qs(parsed.query)
    assert "redirect_uri" in qs
    assert qs["link"][0] == "https://localhost"

    del payload["default_redirect_uri"]
    test_4 = get_message_url(post=payload, app_id=None,
                             link="https://localhost",
                             display=None, to=None, redirect_uri="127.0.0.1",
                             mobile=is_mobile)
    parsed = parse.urlparse(test_4)
    qs = parse.parse_qs(parsed.query)
    assert "redirect_uri" in qs
    assert qs["redirect_uri"][0] == "127.0.0.1"

    del payload["default_to"]

    test_5 = get_message_url(post=payload, app_id=None,
                             link="https://localhost",
                             display=None, to='predator',
                             redirect_uri="127.0.0.1",
                             mobile=is_mobile)
    parsed = parse.urlparse(test_5)
    qs = parse.parse_qs(parsed.query)
    assert "to" in qs
    assert qs["to"][0] == "predator"


def test_get_publication_url(publication_payload, monkeypatch):
    payload = publication_payload
    test_1 = get_publication_url(post=payload, app_id=12345, link=None,
                                 display=None, to=None, redirect_uri=None,
                                 source=None, fb_from=None
                                 )
    parsed = parse.urlparse(test_1)
    qs = parse.parse_qs(parsed.query)
    assert "app_id" in qs
    assert qs["app_id"][0] == "12345"
    assert "link" in qs
    assert qs["link"][0] == "http://fbroadrunner"
    assert "redirect_uri" in qs
    assert qs["redirect_uri"][0] == "http://fbroadrunner"
    assert "to" in qs
    assert qs["to"][0] == "fbroadrunner"
    assert "from" in qs
    assert qs["from"][0] == "alien"
    assert "source" in qs
    assert qs["source"][0] == "predator"

    monkeypatch.setenv('FB_APP_ID', 5555)
    test_2 = get_publication_url(post=payload, link=None, app_id=None,
                                 display=None, to=None, redirect_uri=None,
                                 source=None, fb_from=None)
    parsed = parse.urlparse(test_2)
    qs = parse.parse_qs(parsed.query)
    assert "app_id" in qs
    assert qs["app_id"][0] == "5555"

    del payload["default_link"]
    test_3 = get_publication_url(post=payload, app_id=None,
                                 link="https://localhost",
                                 display=None, to=None, redirect_uri=None,
                                 source=None, fb_from=None)
    parsed = parse.urlparse(test_3)
    qs = parse.parse_qs(parsed.query)
    assert "redirect_uri" in qs
    assert qs["link"][0] == "https://localhost"

    del payload["default_redirect_uri"]
    test_4 = get_publication_url(post=payload, app_id=None,
                                 link="https://localhost",
                                 display=None, to=None,
                                 redirect_uri="127.0.0.1",
                                 source=None, fb_from=None)
    parsed = parse.urlparse(test_4)
    qs = parse.parse_qs(parsed.query)
    assert "redirect_uri" in qs
    assert qs["redirect_uri"][0] == "127.0.0.1"

    del payload["default_to"]
    test_5 = get_publication_url(post=payload, app_id=None,
                                 link="https://localhost",
                                 display=None, to='predator',
                                 redirect_uri="127.0.0.1",
                                 source=None, fb_from=None)
    parsed = parse.urlparse(test_5)
    qs = parse.parse_qs(parsed.query)
    assert "to" in qs
    assert qs["to"][0] == "predator"

    del payload["default_from"]
    test_6 = get_publication_url(post=payload, app_id=None,
                                 link="https://localhost",
                                 display=None, to='predator',
                                 redirect_uri="127.0.0.1",
                                 source=None,
                                 fb_from="mario")
    parsed = parse.urlparse(test_6)
    qs = parse.parse_qs(parsed.query)
    assert "from" in qs
    assert qs["from"][0] == "mario"

    del payload["default_source"]
    test_7 = get_publication_url(post=payload, app_id=None,
                                 link="https://localhost",
                                 display=None, to='predator',
                                 redirect_uri="127.0.0.1",
                                 fb_from="mario",
                                 source="shenmue")
    parsed = parse.urlparse(test_7)
    qs = parse.parse_qs(parsed.query)
    assert "source" in qs
    assert qs["source"][0] == "shenmue"


def test_get_app_id_from_env(monkeypatch):
    app_id = get_app_id_from_env()
    assert app_id is None
    monkeypatch.setenv('FB_APP_ID', 666)
    app_id = get_app_id_from_env()
    assert app_id == 666
