import psutil
from datetime import datetime
import asyncio
from utils.config import Config
import requests


config = Config('config/config.json')

def check_procces(name: str):
    for procc in psutil.process_iter(['name']):
        name_procc = procc.info['name'].lower()
        if name_procc == f'{name.lower()}.exe':
            return True
    return False

def get_request(route: str, data_name: str):
    curr_time = datetime.now().time().strftime('%H')
    requests.get(
        f'http://{config.host}:{config.port}/{route}', 
        headers={'Authorization': config.token},
        json={data_name:curr_time},
    )

async def send_request_every_minute(learn_name: str, code_name: str):
    while True:
            cur_date = datetime.now().date()
            await asyncio.sleep(5)
            if check_procces(learn_name) and check_procces(code_name):
                get_request(route='learn', data_name='hours')
                get_request(route='code', data_name='hours')

            elif check_procces(learn_name): 
                 get_request(route='learn', data_name='hours')

            elif check_procces(code_name): 
                 get_request(route='code', data_name='hours')
                 
            date_now = datetime.now().date()
            if cur_date != date_now:
                get_request(route='save-data', data_name='date')
