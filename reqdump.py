"""dump HTTP communication invoked by requests"""

from sys import stdout


def dump(res, *args, **kw):
    """dump HTTP request and response"""
    # request spec
    method = res.request.method
    url = res.url
    println('> %s %s' % (method, url))

    # request headers
    for k, v in res.request.headers.items():
        println('> %s: %s' % (k, v))

    # reqeuest body
    body = res.request.body
    if body:
        println(body)
    println('')

    # response code
    println('< %s %s' % (res.status_code, res.reason))

    # response headers
    for k, v in res.headers.items():
        println('< %s: %s' % (k, v))

    # response body
    println(res.content)
    println('')


def println(text):
    stdout.write(text + '\n')


if __name__ == '__main__':
    # test
    import requests
    requests.get('http://example.com/', hooks=dict(response=dump))
