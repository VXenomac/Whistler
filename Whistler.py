import requests
from configparser import ConfigParser


class Whistler(object):
    def __init__(self):
        self.cp = ConfigParser()
        self.cp.read('key.conf')
        self.SERVER_CHAN_SCKEY = self.cp.get('KEY', 'SERVER_CHAN_SCKEY')
        self.SERVER_CHAN_URL = self.cp.get(
            'URL', 'SERVER_CHAN_URL') + self.SERVER_CHAN_SCKEY + '.send'
        self.BARK_KEY = self.cp.get('KEY', 'BARK_KEY')
        self.BARK_URL = self.cp.get('URL', 'BARK_URL') + self.BARK_KEY + '/'

    def server_chan(self, text, desp=None):
        if self.SERVER_CHAN_SCKEY:
            requests.get(self.SERVER_CHAN_URL, params={
                         'text': text, 'desp': desp})
        else:
            print('请先填写 SERVER_CHAN_SCKEY')

    def bark(self, title, body, url=None, automaticallyCopy=None, copy=None):
        if self.BARK_KEY:
            print(self.BARK_URL)
            requests.get(self.BARK_URL, params={
                         'title': title, 'body': body, 'url': url, 'automaticallyCopy': automaticallyCopy, 'copy': copy})
        else:
            print('请先填写 BARK_KEY')


if __name__ == '__main__':
    whistler = Whistler()
