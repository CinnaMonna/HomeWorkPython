def view_data(data):
    print(data)

def incorrect_input():
    print('неверное значение')

def get_choice():
    return int(input('''выберите режим - введите 1 или 2:
    1 - вывод телефонного справочника
    2 - добавление информации в справочник\n '''))

def get_new_data():
    new_data = (input('введите фамилию: '), input('введите имя: '), \
                input('введите телефон: '), input('введите информацию: '),)
    return new_data

