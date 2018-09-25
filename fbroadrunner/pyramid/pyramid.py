from json import JSONDecodeError

from fbroadrunner.functions import get_message_url, get_publication_url


def fb_messenger(app_id=None, link=None, redirect_uri=None, display=None,
                 to=None, mobile=False):
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
            url = get_message_url(post=post, app_id=app_id, to=to, link=link,
                                  display=display, redirect_uri=redirect_uri,
                                  mobile=mobile)
            result = func(request, fb_url=url)
            return result

        return wrapper

    return message


def fb_publication(redirect_uri=None, link=None, app_id=None, display=None,
                   to=None, fb_from=None, source=None, is_json=False):
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
            try:
                if is_json:
                    post = request.json_body
                else:
                    if request.POST:
                        post = request.POST
                    else:
                        post = {}
            except JSONDecodeError:
                return func(request, fb_url="")
            url = get_publication_url(post, app_id, link, display,
                                      redirect_uri, to, fb_from, source)
            return func(request, fb_url=url)

        return wrapper

    return publicated
