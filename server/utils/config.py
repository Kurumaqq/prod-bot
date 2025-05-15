import json

class Config():
    def __init__(self, path: str):
        self.config = json.load(open(path, 'r'))

    @property
    def host(self):
        return self.config['host']
    @property
    def port(self):
        return self.config['port']
    @property
    def token(self):
        return self.config['token']
    @property
    def frong_token_error(self):
        return self.config['frong_token_error']
