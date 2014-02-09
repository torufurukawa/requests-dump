#!/usr/bin/env python

from unittest import TestCase
from mock import Mock, patch
import requests
import reqdump


class DumpTestCase(TestCase):
    @patch('reqdump._println')
    def test(self, println):
        # given: make response object contain known values
        res = Mock()
        res.request.method = 'GET'
        res.url = 'http://example.com/'
        res.request.headers = {'foo': 'bar'}
        res.headers = {'myheader': 'myvalue'}

        # when: call dump function
        reqdump.dump(res)

        # then: println is called
        self.assertEqual(println.call_count, 8)
        self.assertEqual(println.call_args_list[0],
                         (('> %s %s' % (res.request.method, res.url),), {}))


class PatchTestCase(TestCase):
    def setUp(self):
        self.original_get = requests.get
        self.original_options = requests.options

    def tearDown(self):
        requests.get = self.original_get
        requests.options = self.original_options

    def test(self):
        # given: requests.get is not patched
        self.assertEqual(requests.get, self.original_get)

        # when: patch
        reqdump.patch_all()

        # then: reqeusts.get is patched
        self.assertEqual(requests.get, reqdump.get)
        self.assertEqual(requests.options, reqdump.options)

        # when: unpatch
        reqdump.unpatch_all()

        # then: requests.get is the original function
        self.assertEqual(requests.get, self.original_get)
        self.assertEqual(requests.options, self.original_options)


class GetTestCase(TestCase):
    def test(self):
        for method_name in ['get', 'options', 'head', 'post', 'put', 'patch',
                            'delete']:
            self._test(method_name)

    def _test(self, method_name):
        # given: original requests function is mocked
        with patch('requests.%s' % method_name) as original_func:

            # when: call reqdump method function
            url = 'http://example.com/'
            kw = {'x': None, 'y': 'xyzzy'}
            result = getattr(reqdump, method_name)(url, **kw)

            # then: original function is called with hook
            kw2 = {}
            kw2.update(kw)
            kw2['hooks'] = {'response': reqdump.dump}
            self.assertEqual(original_func.call_count, 1)
            self.assertEqual(original_func.call_args, ((url, ), kw2))
            self.assertEqual(result, original_func.return_value)
