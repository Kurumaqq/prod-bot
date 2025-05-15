from flask import request
from utils.config import Config
from utils.utils import add_time, save_graph
import os
import json

config = Config('config/config.json')

def add_learn_time():
    token = request.headers.get('Authorization')
    hours = request.get_json()['hours']
    if token == config.token:
        add_time(
            name='learn', 
            path='config/data.json',
            hours=hours
        )
        return '200'
    return config.frong_token_error

def add_code_time():
    token = request.headers.get('Authorization')
    hours = request.get_json()['hours']
    if token == config.token:
        add_time(
            name='code', 
            path='config/data.json',
            hours=hours
        )
        return '200'
    return config.frong_token_error

def save_data():
    token = request.headers.get('Authorization')
    if token == config.token:
        date = request.get_json()['date']
        os.mkdir(f'save/{date}')
        with open('config/data.json', 'r') as f: 
            data = json.load(f)

        with open(f'save/{date}/{date}.json', 'w')as f:
            json.dump(data, f, indent=4)

        save_graph(f'save/{date}/{date}', data)
        return '200'
    return config.frong_token_error

def save_temp_data():
    token = request.headers.get('Authorization')
    if token == config.token:
        name = request.get_json()['name']
        with open('config/data.json', 'r') as f:
            data = json.load(f)

        with open(f'temp/{name}.json', 'w')as f:
            json.dump(data, f, indent=4)

        save_graph(f'temp/{name}', data)
        return '200'
    return config.frong_token_error

