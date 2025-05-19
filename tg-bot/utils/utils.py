import json
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
    while times.minutes >= 60: 
        times.minutes -= 60
        times.hours += 1

def get_saves(path: str):
    saves_dir = Path(path)
    return [
        str(i).split('\\')[-1].split('/')[-1] 
        for i in saves_dir.iterdir()
    ] 

def get_time(time: Times, path: str, name: str):
    time.minutes = get_minutes(name, path) 
    to_hours(time)

def get_caption(code_times: Times, learn_times: Times):
    return (
        f"💻 CODE TIME: {code_times.hours} hours {code_times.minutes} minutes\n"
        f"🧠 LEARN TIME: {learn_times.hours} hours {learn_times.minutes} minutes"
    )
