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

def get_request(route: str, data_name: str):
    curr_time = datetime.now().time().strftime('%H')
    if curr_time == '00': curr_time = '0'
    elif curr_time[0] == '0': curr_time = curr_time[1]
    requests.get(
        f'http://{config.host}:{config.port}/{route}', 
        headers={'Authorization': config.token},
        json={data_name:curr_time},
    )

def send_request_every_minute(learn_name: str, code_name: str):
    while True:
        cur_date = datetime.now().date()
        try:
            if check_procces(learn_name): 
                get_request(route='learn', data_name='hours')

            if check_procces(code_name): 
                get_request(route='code', data_name='hours')
            sleep(60)
            headers = {'Authorization': config.token}
            requests.get(
                f'http://{config.host}:{config.port}/save-data',
                headers=headers,
                json={'date': cur_date.strftime('%Y-%m-%d')}
            )
        except: continue
