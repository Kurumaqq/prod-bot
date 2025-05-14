from flask import Flask, request
from config import Config
from datetime import datetime
from save_graph import save_graph
import json
import os

app = Flask(__name__)
config = Config('config/config.json')

# TODO: move in other file
# TODO: rename error code (500)
@app.route('/learn', methods=['GET'])
def add_time_learn():
    token = request.headers.get('Authorization')
    hours =request.get_json()['hours']
    if token == config.token:
        with open('config/data.json', 'r') as f:
            data = json.load(f)
        with open('config/data.json', 'w') as f:
            if f'learn_time_{hours}' in data:            
                data[f'learn_time_{hours}'] += 1
            else: data[f'learn_time_{hours}'] = 1
            json.dump(data, f, indent=4)
        return '200'
    return '500'

@app.route('/code', methods=['GET'])
def add_code_time():
    token = request.headers.get('Authorization')
    hours = request.get_json()['hours']
    if token == config.token:
        with open('config/data.json', 'r') as f:
            data = json.load(f)
        with open('config/data.json', 'w') as f:
            if f'code_time_{hours}' in data:            
                data[f'code_time_{hours}'] += 1
            else: data[f'code_time_{hours}'] = 1
            json.dump(data, f, indent=4)
        return '200'
    return '500'

@app.route('/save-data', methods=['POST'])
def save_data():
    token = request.headers.get('Authorization')
    if token == config.token:
        date = request.get_json()['date']
        os.mkdir(f'save/{date}')
        with open('config/data.json', 'r') as f:
            data = json.load(f)
        with open(f'save/{date}/{date}.json', 'w')as f:
            json.dump(data, f, indent=4)
    return '200'

@app.route('/save-graph', methods=['GET'])
def save_graph():
    name = datetime.now().date()
    token = request.headers.get('Authorization')
    if token == config.token:
        with open('config/data.json', 'r') as f:
            data = json.load(f)
        save_graph(f'temp/{name}', data)
        return '200'

@app.route('/get-data', methods=['POST'])
def del_graph():
    token = request.headers.get('Authorization')
    if token == config.token:
        name = request.get_json()['name']
        os.remove(f'temp/{name}')
        
if __name__ == '__main__':
    app.run()
