import os
from urllib import parse

from fbroadrunner.exceptions import FbRoadRunnerFieldError
from fbroadrunner.validators.schema import CustomNormalizer
from fbroadrunner.validators.schema import MESSAGE_SCHEMA, PUBLICATION_SCHEMA

FACEBOOK_DIALOG_WEB = "https://www.facebook.com/dialog/feed?{}"
MESSAGE_DIALOG_WEB = "http://www.facebook.com/dialog/send?{}"
MESSAGE_DIALOG_MOBILE = "fb-messenger://share?{}"


def get_app_id_from_env():
    try:
        fb_app_id = int(os.getenv('FB_APP_ID'))
    except (ValueError, TypeError):
        fb_app_id = None
    return fb_app_id


def validate_and_normalize_payload(payload, schema):
    validator = CustomNormalizer(schema)
    normalized = validator.normalized(payload)
    # Purge unknown fields
    purge_unknown = {k: v for k, v in normalized.items() if k in schema}
    if not validator.validate(purge_unknown):
        raise FbRoadRunnerFieldError(validator.errors)
    # Removing None values
    return {k: v for k, v in purge_unknown.items() if v is not None}


def get_message_url(post, app_id, link, display, to, redirect_uri, mobile):
    post['app_id'] = app_id if app_id else get_app_id_from_env()
    post['default_link'] = post[
        'default_link'] if 'default_link' in post else link
    post['default_display'] = post[
        'default_display'] if 'default_display' in post else display
    post['default_redirect_uri'] = post[
        'default_redirect_uri'] if 'default_redirect_uri' in post else redirect_uri
    post['default_to'] = post['default_to'] if 'default_to' in post else to
    normalized_payload = validate_and_normalize_payload(post,
                                                        MESSAGE_SCHEMA)

    if mobile:
        url = MESSAGE_DIALOG_MOBILE.format(
            parse.urlencode(normalized_payload))
    else:
        url = MESSAGE_DIALOG_WEB.format(
            parse.urlencode(normalized_payload))
    return url


def get_publication_url(post, app_id, link, display, redirect_uri, to, fb_from,
                        source):
    post['app_id'] = app_id if app_id else get_app_id_from_env()
    post['default_link'] = post[
        'default_link'] if 'default_link' in post else link
    post['default_display'] = post[
        'default_display'] if 'default_display' in post else display
    post['default_redirect_uri'] = post[
        'default_redirect_uri'] if 'default_redirect_uri' in post else redirect_uri
    post['default_to'] = post['default_to'] if 'default_to' in post else to
    post['default_from'] = post[
        'default_from'] if 'default_from' in post else fb_from
    post['default_source'] = post[
        'default_source'] if 'default_source' in post else source
    normalized_payload = validate_and_normalize_payload(post,
                                                        PUBLICATION_SCHEMA)
    url = FACEBOOK_DIALOG_WEB.format(
        parse.urlencode(normalized_payload))
    return url
