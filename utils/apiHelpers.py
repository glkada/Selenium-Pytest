import http.client
from settings import Settings

class ApiHelper:
    def __init__(self):
        settings = Settings()
        self.conn = http.client.HTTPConnection(settings.HOST.split("/")[2])
        self.payload = ''
        self.headers = {
          'Accept': 'application/json, text/plain, */*',
          'Accept-Language': 'en-US,en;q=0.5',
          'Connection': 'keep-alive'
        }
    def reqeust(self, method: str, api: str, *args):
        if len(args) > 0:  self.payload = args[0]   # if payload is sent as an argument we consider it
        try:
            self.conn.request(method, api, self.payload, self.headers)
        except ConnectionError as connError:
            print(connError)
        res = self.conn.getresponse()
        data = res.read()
        if res.getcode() == 200:
            return data.decode("utf-8")
        else:
            raise Exception(f'API response: {res.getcode()}')