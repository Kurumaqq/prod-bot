import json

class Config():
    def __init__(self, path: str):
        self.path = path

    @property
    def host(self):
        with open(self.path, 'r') as f:
            return json.load(f)['host']
        
    @property
    def port(self):
        with open(self.path, 'r') as f:
            return json.load(f)['port']
        
    @property
    def token(self):
        with open(self.path, 'r') as f:
            return json.load(f)['token']

    @property
    def headers(self):
        with open(self.path, 'r') as f:
            return {'Authorization': f'Bearer {json.load(f)['token']}'}
    @property
    def url(self):
        return f'http://{self.host}:{self.port}'

    @property
    def bot_token(self):
        with open(self.path, 'r') as f:
            return json.load(f)['bot_token']
