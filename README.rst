requets-dump
============

Provides a hook function to dump HTTP communiation for requests.

Please, Please, Please note that this library is in pre-alpha phase and
its interface is subject to change.

Usage
-----

You may pass the hook function to a requests' method function.

::

    >>> import requests
    >>> import reqdump
    >>> requests.get('http://example.com/', hooks=dict(response=reqdump.dump))
    > GET http://example.com/
    > Accept-Encoding: gzip, deflate, compress
    > Accept: */*
    > User-Agent: python-requests/2.2.1 CPython/2.7.6 Darwin/13.0.2

    < 200 OK
    < content-length: 1270
    < x-ec-custom-error: 1
    < x-cache: HIT
    < accept-ranges: bytes
    < expires: Tue, 11 Feb 2014 13:41:46 GMT
    < server: ECS (sjc/4FB4)
    < last-modified: Fri, 09 Aug 2013 23:54:35 GMT
    < etag: "359670651"
    < cache-control: max-age=604800
    < date: Tue, 04 Feb 2014 13:41:46 GMT
    < content-type: text/html
    <!doctype html>
    <html>
    (... snip ...)
    <Response [200]>
    >>>

You can also apply patch to all requests' method functions to use the hook
function.

::

    >>> import requests
    >>> import reqdump
    >>> reqdump.patch()
    >>> requests.get('http://example.com/')
    > GET http://example.com/
    > Accept-Encoding: gzip, deflate, compress
    (... snip ...)
    <Response [200]>
    >>> reqdump.unpatch()  # discard patches
    >>> requests.get('http://example.com/')
    <Response [200]>
    >>>


History
-------

0.1.3
^^^^^

* Rename patch() with patch_all() and unpatch() with unpatch_all()
* Support HTTP methods other than GET

0.1.2
^^^^^

* Add patch() and unpatch() functions

0.1.1
^^^^^

* Support Python 3.3

0.1
^^^

* Birth!
