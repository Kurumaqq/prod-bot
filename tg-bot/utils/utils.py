import json
from datetime import datetime
from pathlib import Path

class Times():
    hours = 0
    minutes = 0

def get_minutes(name: str, path: str):
    with open(path, 'r') as f:
        data = json.load(f)
    minutes = 0
    for i in data:
        if i.split('_')[0] == name:
            minutes += data[i]
    return minutes

def to_hours(times: Times):
    while times.minutes > 60: 
        times.minutes -= 60
        times.hours += 1

def get_saves(path: str):
    saves_dir = Path(path)
    return [
        str(i).split('\\')[-1].split('/')[-1] 
        for i in saves_dir.iterdir()
    ] 
