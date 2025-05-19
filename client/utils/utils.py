import psutil
from datetime import datetime
from time import sleep
from utils.config import Config
import requests


config = Config('config/config.json')

def check_procces(name: str):
    for procc in psutil.process_iter(['name']):
        name_procc = procc.info['name'].lower()
        if name_procc == f'{name.lower()}.exe':
            return True
    return False

def send_request_add_time(name: str):
    curr_time = datetime.now().time().strftime('%H')
    headers = {'Authorization': config.token}
    if curr_time == '00': curr_time = '0'
    elif curr_time[0] == '0': curr_time = curr_time[1]
    requests.post(
        f'http://{config.host}:{config.port}/add-time/{name}', 
        headers=headers,
        params={'hours': curr_time},
    )

def send_request_every_minute(learn_name: str, code_name: str):
    while True:
        cur_date = datetime.now().date().strftime('%Y-%m-%d')
        try:
            if check_procces(learn_name): 
                send_request_add_time(name='learn')

            if check_procces(code_name): 
                send_request_add_time(name='code')

            headers = {'Authorization': config.token}
            requests.post(
                f'http://{config.host}:{config.port}/save',
                headers=headers,
                params={'date': cur_date}
            )
            sleep(60)
        except: continue
