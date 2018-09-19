import os


def get_app_id_from_env():
    try:
        fb_app_id = int(os.getenv('FB_APP_ID'))
    except (ValueError, TypeError):
        fb_app_id = None
    return fb_app_id
