from flask import Flask
from utils.rule import *

def load_rule(app: Flask):
    rule_learn(app)
    rule_code(app)
    rule_save_data(app)
    rule_save_graph(app)

def rule_learn(app: Flask):
    app.add_url_rule(
        rule='/learn', 
        endpoint='learn', 
        view_func=add_learn_time,
        methods=['GET']
    )

def rule_code(app: Flask):
    app.add_url_rule(
        rule='/code', 
        endpoint='code', 
        view_func=add_code_time,
        methods=['GET']
    )

def rule_save_data(app: Flask):
    app.add_url_rule(
        rule='/save-data', 
        endpoint='save-data', 
        view_func=save_data,
        methods=['GET']
    )

def rule_save_graph(app: Flask):
    app.add_url_rule(
        rule='/save-temp-data', 
        endpoint='save-graph', 
        view_func=save_temp_data,
        methods=['GET']
    )
