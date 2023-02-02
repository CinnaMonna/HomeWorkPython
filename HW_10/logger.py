from datetime import datetime

def logger(id, action, data):
    time = datetime.now()
    with open('HW_10\log.csv', 'a') as file:
        file.write(f'{time}: {id}: {action}   result: {data}\n')
