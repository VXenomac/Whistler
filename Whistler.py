import requests
from configparser import ConfigParser


class Whistler(object):
    def __init__(self, server_chan=None, bark=None):
        if server_chan:
            self.SERVER_CHAN_SCKEY = server_chan
            self.SERVER_CHAN_URL = 'https://sc.ftqq.com/' + self.SERVER_CHAN_SCKEY + '.send'
        if bark:
            self.BARK_KEY = bark
            self.BARK_URL = 'https://api.day.app/' + self.BARK_KEY + '/'

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
    cp = ConfigParser()
    cp.read('key.conf')
    SERVER_CHAN_SCKEY = cp.get('KEY', 'SERVER_CHAN_SCKEY')
    BARK_KEY = cp.get('KEY', 'BARK_KEY')
    whistler = Whistler(SERVER_CHAN_SCKEY, BARK_KEY)
