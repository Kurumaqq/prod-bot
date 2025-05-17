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
    def frong_token_error(self):
        with open(self.path, 'r') as f:
            return json.load(f)['frong_token_error']
    
    @property
    def last_date(self):
        with open(self.path, 'r') as f:
            return json.load(f)['last_date']
        
    @last_date.setter
    def last_date(self, value):
        with open(self.path, 'r') as f: data = json.load(f)
        data['last_date'] = value
        with open(self.path, 'w') as f: json.dump(data, f, indent=4)
