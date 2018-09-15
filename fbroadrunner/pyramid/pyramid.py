import os

from fbroadrunner.errors import FbRoadRunnerFieldError
from ..validators.schema import CustomNormalizer, PUBLICATION_SCHEMA, MESSAGE_SCHEMA
from urllib import parse

FACEBOOK_DIALOG_WEB = "https://www.facebook.com/dialog/feed?{}"
MESSAGE_DIALOG_WEB = "http://www.facebook.com/dialog/send?{}"
MESSAGE_DIALOG_MOBILE = "fb-messenger://share?{}"


def _get_app_id_from_env():
    try:
        fb_app_id = int(os.getenv('FB_APP_ID'))
    except (ValueError, TypeError):
        fb_app_id = None
    return fb_app_id


def _validate_and_normalize_payload(payload, schema):
    validator = CustomNormalizer(schema)
    normalized = validator.normalized(payload)
    # Purge unknown fields
    purge_unknown = {k: v for k, v in normalized.items() if k in schema}
    if not validator.validate(purge_unknown):
        raise FbRoadRunnerFieldError(validator.errors)
    # Removing None values
    return {k: v for k, v in purge_unknown.items() if v is not None}


def fb_messenger(app_id=None, link=None, redirect_uri=None, display=None, to=None, mobile=False):
    """
    This decorator help us to build a share facebook messenger url
    :param app_id: Your app's unique identifier. Required.
    :param link: The link attached to this message.
    :param redirect_uri: The URL to redirect to after a person clicks a button on the dialog
    :param display: Determines how the dialog is rendered.
    :param to: The ID of the profile that this message will be send
    :param mobile: True or False
    :return:
    """
    def message(func):
        def wrapper(request, *args, **kwargs):
            nonlocal app_id
            nonlocal mobile
            nonlocal link
            nonlocal to
            nonlocal display
            post = request.POST
            post['app_id'] = app_id if app_id else _get_app_id_from_env()
            post['default_link'] = link
            post['default_display'] = display
            post['default_redirect_uri'] = redirect_uri
            post['default_to'] = to
            mobile = True if 'fb_is_mobile' in request.POST else mobile
            normalized_payload = _validate_and_normalize_payload(post, MESSAGE_SCHEMA)

            if mobile:
                url = MESSAGE_DIALOG_MOBILE.format(parse.urlencode(normalized_payload))
            else:
                url = MESSAGE_DIALOG_WEB.format(parse.urlencode(normalized_payload))
            result = func(request, fb_url=url)
            return result

        return wrapper

    return message


def fb_publication(redirect_uri=None, link=None, app_id=None, display=None, to=None, fb_from=None, source=None):
    """
    This decorator help us to build a share facebook publisher url
    :param redirect_uri: The URL to redirect to after a person clicks a button on the dialog
    :param link: The link attached to this post.
    :param app_id: Your app's unique identifier. Required.
    :param display: Determines how the dialog is rendered.
    :param to: The ID of the profile that this story will be published to
    :param fb_from: The ID of the person posting the message
    :param source: The URL of a media file (either SWF or MP3) attached to this post
    :return: feed dialog url
    """

    def publicated(func):
        def wrapper(request, *args, **kwargs):
            nonlocal app_id
            nonlocal display
            nonlocal link
            nonlocal redirect_uri
            nonlocal to
            nonlocal fb_from
            nonlocal source
            post = request.POST
            post['app_id'] = app_id if app_id else _get_app_id_from_env()
            post['default_link'] = link
            post['default_display'] = display
            post['default_redirect_uri'] = redirect_uri
            post['default_to'] = to
            post['default_from'] = fb_from
            post['default_source'] = source
            normalized_payload = _validate_and_normalize_payload(post, PUBLICATION_SCHEMA)
            url = FACEBOOK_DIALOG_WEB.format(parse.urlencode(normalized_payload))
            result = func(request, fb_url=url)
            return result

        return wrapper

    return publicated
