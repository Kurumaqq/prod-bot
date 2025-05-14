from datetime import datetime
from config import Config
import requests
import asyncio
import psutil 
import json

# TODO: create utils and move there
def check_procces(name: str):
    for procc in psutil.process_iter(['name']):
        name_procc = procc.info['name'].lower()
        if name_procc == f'{name.lower()}.exe':
            return True
    return False

async def send_request_every_minute(learn_name: str, code_name: str):
    while True:
            cur_time = datetime.now().time().strftime('%H')
            cur_date = datetime.now().date()
            await asyncio.sleep(5)
            # TODO: create get func 
            if check_procces(learn_name) and check_procces(code_name):
                requests.get(
                    f'http://{config.host}:{config.port}/learn', 
                    headers=headers,
                    json={'hours':cur_time},
                )
                requests.get(
                    f'http://{config.host}:{config.port}/code', 
                    headers=headers,
                    json={'hours':cur_time},
                )
            elif check_procces(learn_name):
                requests.get(
                    f'http://{config.host}:{config.port}/learn', 
                    headers=headers,
                    json={'hours':cur_time},
                )
            elif check_procces(code_name): 
                requests.get(
                    f'http://{config.host}:{config.port}/code', 
                    headers=headers,
                    json={'hours':cur_time},
                )
            date_now = datetime.now().date()
            if cur_date != date_now:
                requests.get(
                    f'http://{config.host}:{config.port}/save_data', 
                    headers=headers,
                    json={'date':date_now},
                )
            
if __name__ == '__main__':
    with open('config.json', 'r') as f: config = json.load(f)
    config = Config('config.json')
    headers = {'Authorization': config.token}

    asyncio.run(send_request_every_minute(config.learn_name, config.code_name))
    