from flask import Flask, request
from config import Config
import json

app = Flask(__name__)
config = Config('config.json')


@app.route('/learn')
def add_time_learn():
    token = request.headers.get('Authorization')
    hours =request.get_json()['hours']
    if token == config.token:
        with open('../tg-bot/data.json', 'r') as f:
            data = json.load(f)
        with open('../tg-bot/data.json', 'w') as f:
            data[f'learn_time_{hours}'] += 1
            json.dump(data, f, indent=4)
        return '200'
    return '500'

@app.route('/code')
def add_code_time():
    token = request.headers.get('Authorization')
    hours = request.get_json()['hours']
    if token == config.token:
        with open('../tg-bot/data.json', 'r') as f:
            data = json.load(f)
        with open('../tg-bot/data.json', 'w') as f:
            data[f'code_time_{hours}'] += 1
            json.dump(data, f, indent=4)
        return '200'
    return '500'

if __name__ == '__main__':
    app.run()
