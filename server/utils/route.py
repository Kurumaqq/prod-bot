from fastapi import APIRouter, Request, HTTPException
from utils.utils import add_time_data, save_graph
from utils.config import Config
import json
import os

router = APIRouter()
config = Config('config/config.json')

@router.post('/add-time/{app}')
def add_time(hours: str, app: str, request: Request):
    headers = request.headers
    token = headers['Authorization'] if 'Authorization' in headers else ''
    if token == config.token:
        add_time_data(
            name=app, 
            path='config/data.json',
            hours=hours
        )
        return {'success': True}
    raise HTTPException(status_code=401, detail='invalid token')

@router.post('/save')
def save_data(date: str, request: Request):
    headers = request.headers
    token = headers['Authorization'] if 'Authorization' in headers else ''
    last_date = config.last_date
    if token == config.token and last_date != date:
        os.mkdir(f'saves/{last_date}')
        with open('config/data.json', 'r') as f: 
            data = json.load(f)

        with open(f'saves/{last_date}/{last_date}.json', 'w')as f:
            json.dump(data, f, indent=4)

        save_graph(f'saves/{last_date}/{last_date}', data)
        with open(f'config/data.json', 'w') as f:
            json.dump({}, f, indent=4)
        config.last_date = date
        return {'success': True}
    return HTTPException(status_code=401, detail='invalid token')

@router.post('/save/temp')
def save_temp_data(date: str, request: Request):
    headers = request.headers
    token = headers['Authorization'] if 'Authorization' in headers else ''
    if token == config.token:
        with open('config/data.json', 'r') as f:
            data = json.load(f)

        with open(f'temp/{date}.json', 'w')as f:
            json.dump(data, f, indent=4)

        save_graph(f'temp/{date}', data)
        return {'success': True}
    return HTTPException(status_code=401, detail='invalid token')
