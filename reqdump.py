"""dump HTTP communication invoked by requests"""

from sys import stdout
import requests


# --------------------------------------------------------------
# Hook function
# --------------------------------------------------------------

def dump(res, *args, **kw):
    """dump HTTP request and response"""
    # request spec
    method = res.request.method
    url = res.url
    _println('> %s %s' % (method, url))

    # request headers
    for k, v in res.request.headers.items():
        _println('> %s: %s' % (k, v))

    # reqeuest body
    body = res.request.body
    if body:
        _println(body)
    _println('')

    # response code
    _println('< %s %s' % (res.status_code, res.reason))

    # response headers
    for k, v in res.headers.items():
        _println('< %s: %s' % (k, v))

    # response body
    _println(res.text)
    _println('')


def _println(text):
    stdout.write(text)
    stdout.write('\n')


# --------------------------------------------------------------
# Monkey patch
# --------------------------------------------------------------

# store original functions
_ORIGINAL_FUNCS = dict([(method_name, getattr(requests, method_name))
                        for method_name
                        in ['get', 'options', 'head', 'post', 'put', 'patch',
                            'delete']])


def patch_all():
    for method_name in ['get', 'options']:
        setattr(requests, method_name, globals()[method_name])


def unpatch_all():
    for method_name, func in _ORIGINAL_FUNCS.items():
        setattr(requests, method_name, func)


def _wrap(method_name):
    def inner(*args, **kw):
        f = getattr(requests, method_name)
        return f(*args, hooks={'response': dump}, **kw)
    return inner


# define wrappers
get = _wrap('get')
options = _wrap('options')
head = _wrap('head')
post = _wrap('post')
put = _wrap('put')
patch = _wrap('patch')
delete = _wrap('delete')
