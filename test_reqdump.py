#!/usr/bin/env python

from unittest import TestCase
from mock import Mock, patch

from reqdump import dump


class DumpTestCase(TestCase):
    @patch('reqdump.println')
    def test(self, println):
        # given: make response object contain known values
        res = Mock()
        res.request.method = 'GET'
        res.url = 'http://example.com/'
        res.request.headers = {'foo': 'bar'}
        res.headers = {'myheader': 'myvalue'}

        # when: call dump function
        dump(res)

        # then: println is called
        self.assertEqual(println.call_count, 8)
        self.assertEqual(println.call_args_list[0],
                         (('> %s %s' % (res.request.method, res.url),), {}))
