from urlparse import urlparse
import requests
from requests.exceptions import TooManyRedirects, HTTPError

class Request(object):
    def __init__(self, host, consumer_key=""):
        self.host = host
        self.headers = {}

    def get(self, url, params=None):
        url = self.host + url

        if params:
            url = url + "?" + urlparse.urlencode(params)

        try:
            resp = requests.get(url, allow_redirects=False, headers=self.headers)
        except TooManyRedirects as e:
            resp = e.response

        return self.parse_json(resp)

    def parse_json(self, response):
        try:
            data = response.json()
        except ValueError:
            data = { "meta": { "status": 500, "msg": "Internal Server Error" }, "response": { "error": "Something went wrong" } }

        return data