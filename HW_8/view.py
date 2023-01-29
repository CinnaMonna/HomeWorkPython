def get_role():
    return int(input('''Введите:
    1, если Вы - учитель
    2, если Вы - ученик\n '''))

def incorrect_input():
    print('неверное значение')

def get_mode():
    return int(input('''Введите:
    1 - добавить новую оценку
    0 - выход\n '''))

def get_lesson():
    return int(input('''Введите предмет:
    0 - математика
    1 - русский яз.
    2 - литература
    3 - биология
    4 - география\n '''))

def get_surname():
    return(input('Введите фамилию: '))

def get_scores():
    return(input('Введите оценки в одну строку через пробел:\n'))