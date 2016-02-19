# -*- coding: utf-8 -*-

import requests

BITLY_API_URL = 'https://api-ssl.bitly.com'
BITLY_SHORTER_URL = BITLY_API_URL + '/v3/shorten'


class BitlyException(Exception):

    def __init__(self, payload):
        super(BitlyException, self).__init__('Can\'t generate short link.')
        self.payload = payload


class Bitly(object):

    def __init__(self, token, domain=None):
        if not token:
            raise ValueError('token is empty.')

        self.token = token
        self.domain = domain or ''

    def shorten(self, url):
        if not url:
            raise ValueError('url is empty.')

        response = requests.get(BITLY_SHORTER_URL, params={
            'domain': self.domain,
            'access_token': self.token,
            'longUrl': url,
            'format': 'json'
        })

        if response.status_code == 200 and response.json().get('status_code') == 200:
            return response.json().get('data', {}).get('url', url)
        else:
            raise BitlyException(response.json())
