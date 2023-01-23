from datetime import datetime

def logger(data, action):
    time = datetime.now()
    with open('HW_7\log.csv', 'a') as file:
        file.write(f'{time}: {action}: {data}\n')
