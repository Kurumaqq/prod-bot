from utils.utils import send_request_every_minute
from utils.config import Config
import asyncio
import json
            
if __name__ == '__main__':
    with open('config/config.json', 'r') as f: config = json.load(f)
    config = Config('config/config.json')

    send_request_every_minute(config.learn_name, config.code_name)
    