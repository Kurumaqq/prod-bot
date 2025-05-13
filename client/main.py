import psutil 
import requests
from time import sleep
import json

def check_procces(name: str):
    for procc in psutil.process_iter(['name']):
        name_procc = procc.info['name'].lower()
        if name_procc == f'{name.lower()}.exe':
            return True
    return False

if __name__ == '__main__':
    with open('config.json', 'r') as f: config = json.load(f)
    learn_name = config['learn_name']
    code_name =config['code_name']
    token = config['token']
    headers = {'Authorization': token}

    while True:
        sleep(5)
        if check_procces(learn_name) and check_procces(code_name):
            requests.get('http://127.0.0.1:5000/learn', headers=headers)
            requests.get('http://127.0.0.1:5000/code', headers=headers)
        elif check_procces(learn_name):
            requests.get('http://127.0.0.1:5000/learn', headers=headers)
        elif check_procces(code_name): 
            requests.get('http://127.0.0.1:5000/code', headers=headers)
        else: print('NO ACTIVES')
