import psutil 
import requests
from time import sleep

def check_procces(name: str):
    for procc in psutil.process_iter(['name']):
        name_procc = procc.info['name'].lower()
        if name_procc == f'{name.lower()}.exe':
            return True
    return False

if __name__ == '__main__':
    while True:
        sleep(60)
        if check_procces('firefox') and check_procces('code'):
            print('LEARN AND CODE')
        elif check_procces('firefox'):
            print('LEARN')
        elif check_procces('code'): 
            print('CODE')
        else: print('NO ACTIVES')
