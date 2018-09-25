[![Coverage Status](https://coveralls.io/repos/github/marcelomoraes28/fbroadrunner/badge.svg?branch=pyramid)](https://coveralls.io/github/marcelomoraes28/fbroadrunner?branch=pyramid)
[![Build Status](https://travis-ci.org/marcelomoraes28/fbroadrunner.svg?branch=master)](https://travis-ci.org/marcelomoraes28/fbroadrunner)
[![Pypi](https://img.shields.io/badge/pypi-0.0.3--alpha-yellow.svg)](https://shields.io)
[![Python](https://img.shields.io/badge/python-3.6-blue.svg)](https://shields.io)


# Fbroadrunner

![alt text](roadrunner.png)

An easy library to help build sharing urls of messages or posts on facebook.

## Getting Started

These instructions will help you install library and use its features.

### Prerequisites

* Python 3
* Pyramid Framework (released)
* Django (released)
* Flask (not implemented)

### Installing

```
pip install fbroadrunner
```

Or you can clone the repository and run

```
pip install -e .
```


## Running the tests
Install test dependencies
```
pip install -e ".[test]"
```

Run test
```
pytest
```

## Using

To start use the library you can setting env FB_APP_ID with your facebook app id.

### Publication parameteres (extracted by [Facebook](https://developers.facebook.com/docs/sharing/reference/feed-dialog))
![alt text](fb_publisher.png)

### Messenger parameters (extracted by [Facebook](https://developers.facebook.com/docs/sharing/reference/send-dialog))

![alt text](fb_message.png)

### Pyramid Framework
 
#### Publication examples
Fixed url link

**CODE**
```python
from pyramid.response import Response
from pyramid.view import view_config
from fbroadrunner import pyramid


@view_config(route_name='fb')
@pyramid.fb_publication(redirect_uri='https://mysite.com', link='https://mysite.com')
def fb(request, **kwargs):
    return Response(kwargs.get('fb_url'))
```

Received link by post

**CODE**
```python
from pyramid.response import Response
from pyramid.view import view_config
from fbroadrunner import pyramid


@view_config(route_name='fb')
@pyramid.fb_publication()
def fb(request, **kwargs):
    return Response(kwargs.get('fb_url'))
```
**POST**
```
curl -d "link=https://mysite.com&redirect_uri=https://mysite.com" -X POST http://localhost/fb
```

If you not set FB_APP_ID, you must use

**CODE**
```python
from pyramid.response import Response
from pyramid.view import view_config
from fbroadrunner import pyramid


@view_config(route_name='fb')
@pyramid.fb_publication(app_id=123456789,redirect_uri='https://mysite.com', link='https://mysite.com')
def fb(request, **kwargs):
    return Response(kwargs.get('fb_url'))
```
#### Send messages examples

Fixed url link

**CODE**
```python
from pyramid.response import Response
from pyramid.view import view_config
from fbroadrunner import pyramid


@view_config(route_name='fb')
@pyramid.fb_messenger(redirect_uri='https://mysite.com', link='https://mysite.com')
def fb(request, **kwargs):
    return Response(kwargs.get('fb_url'))
```

If you're using mobile you should use the example below.

**CODE**
```python
from pyramid.response import Response
from pyramid.view import view_config
from fbroadrunner import pyramid


@view_config(route_name='fb')
@pyramid.fb_messenger()
def fb(request, **kwargs):
    return Response(kwargs.get('fb_url'))
```
**POST**
```
curl -d "link=https://mysite.com&redirect_uri=https://mysite.com&is_mobile=True" -X POST http://localhost/fb
```

Fixed endpoint to return a mobile link

**CODE**
```python
from pyramid.response import Response
from pyramid.view import view_config
from fbroadrunner import pyramid


@view_config(route_name='fb')
@pyramid.fb_messenger(mobile=True, redirect_uri='https://mysite.com', link='https://mysite.com')
def fb(request, **kwargs):
    return Response(kwargs.get('fb_url'))
```

### Flask Framework

#### Publication examples

```python
from flask import Flask
from flask import request
from fbroadrunner.flask import fb_publication

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
@fb_publication(app_id=1234, request=request, is_json=True)
def login(**kwargs):
    return kwargs['fb_url']
```
#### Send messages examples

```python
from flask import Flask, url_for
from flask import request
from fbroadrunner.flask import fb_messenger

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
@fb_messenger(app_id=1234, request=request, is_json=True)
def login(**kwargs):
    return kwargs['fb_url']
```


