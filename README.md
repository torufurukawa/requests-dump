# requets-dump

Dump HTTP communiation by requests.

# Usage

```
>>> import requests
>>> from reqdump import dump
>>> requests.get('http://example.com/', hooks=dict(response=dump))
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
...
```
