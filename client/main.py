import psutil 
import requests
from datetime import datetime
import json
import asyncio

def check_procces(name: str):
    for procc in psutil.process_iter(['name']):
        name_procc = procc.info['name'].lower()
        if name_procc == f'{name.lower()}.exe':
            return True
    return False

async def send_request_every_minute(learn_name: str, code_name: str):
    while True:
            cur_time = datetime.now().time().strftime('%H')
            await asyncio.sleep(5)
            if check_procces(learn_name) and check_procces(code_name):
                requests.get(
                    'http://127.0.0.1:5000/learn', 
                    headers=headers,
                    json={'hours':cur_time},
                )
                requests.get(
                    'http://127.0.0.1:5000/code', 
                    headers=headers,
                    json={'hours':cur_time},
                )
            elif check_procces(learn_name):
                requests.get(
                    'http://127.0.0.1:5000/learn', 
                    headers=headers,
                    json={'hours':cur_time},
                )
            elif check_procces(code_name): 
                requests.get(
                    'http://127.0.0.1:5000/code', 
                    headers=headers,
                    json={'hours':cur_time},
                )
            else: print('NO ACTIVES')
            
if __name__ == '__main__':
    with open('config.json', 'r') as f: config = json.load(f)
    learn_name = config['learn_name']
    code_name =config['code_name']
    token = config['token']
    headers = {'Authorization': token}

    asyncio.run(send_request_every_minute(learn_name, code_name))
    