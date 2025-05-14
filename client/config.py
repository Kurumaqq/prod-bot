import json

class Config():
    def __init__(self, path: str):
        self.config = json.load(open(path, 'r'))

    @property
    def host(self): return self.config['host']
    
    @property
    def port(self): return self.config['port']

    @property
    def learn_name(self): return self.config['learn_name']

    @property
    def code_name(self): return self.config['code_name']

    @property
    def token(self): return self.config['token']
