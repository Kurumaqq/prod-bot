from flask import Flask, request
from utils.config import Config
from utils.load_rule import load_rule

app = Flask(__name__)
config = Config('config/config.json')

load_rule(app)

if __name__ == '__main__':
    app.run(host=config.host, port=config.port)
