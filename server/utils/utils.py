import matplotlib.pyplot as plt
import seaborn as sns
import json

def add_time_data(name: str, path: str, hours:str):
    full_name = f'{name}_time_{hours}'

    with open(path, 'r') as f: data = json.load(f)
    with open(path, 'w') as f:
        if full_name in data: data[full_name] += 1
        else: data[full_name] = 1

        json.dump(data, f, indent=4)

def save_graph(name: str, data: dict):
    plt.style.use('default')  
    sns.set_palette("deep") 

    learn_time = []
    for i in range(0, 24):
        if f'learn_time_{i}' in data:
            learn_time.append(data[f'learn_time_{i}'])
        else: learn_time.append(0)
        
    code_time = []
    for i in range(0, 24):
        if f'code_time_{i}' in data:
            code_time.append(data[f'code_time_{i}'])
        else: code_time.append(0)

    hours = [i for i in range(0, 24)]

    plt.figure(figsize=(10, 6), facecolor='#121212')  # Размер и цвет фона
    sns.lineplot(x=hours, y=code_time, linewidth=8, label='Code')
    sns.lineplot(x=hours, y=learn_time, linewidth=8, label="Learn")

    plt.title("Productivity", fontsize=14, pad=20, color='white')
    plt.xlabel("Hours", fontsize=24)
    plt.ylabel("Minutes", fontsize=24)
    plt.grid(alpha=0.3)

    plt.legend(frameon=False, fontsize=20, loc='upper left')

    plt.savefig(f"{name}.jpg", dpi=300, bbox_inches='tight', transparent=True)
