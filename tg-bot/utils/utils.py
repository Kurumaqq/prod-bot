import json
from datetime import datetime

class Times():
    hours: int
    minutes: int

def get_minutes(name: str):
    with open(f'../server/temp/{datetime.now().date()}.json') as f:
        data = json.load(f)
    minutes = 0
    for i in data:
        if i.split('_')[0] == name:
            minutes += data[i]
    return minutes

def to_hours(minutes: int):
    while minutes > 60: 
        minutes -= 60
        minutes += 1
    return minutes
