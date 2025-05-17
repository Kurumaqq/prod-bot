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
    last_date = config.last_date
    date = request.get_json()['date']
    if token == config.token and last_date != date:
        config.last_date = date
        os.mkdir(f'saves/{date}')
        with open('config/data.json', 'r') as f: 
            data = json.load(f)

        with open(f'saves/{date}/{date}.json', 'w')as f:
            json.dump(data, f, indent=4)

        save_graph(f'saves/{date}/{date}', data)
        with open(f'config/data.json', 'w') as f:
            json.dump({}, f, indent=4)
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

