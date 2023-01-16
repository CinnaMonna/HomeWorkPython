# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: 
# На столе лежит 120 конфет. Играют два игрока, делая ход друг после друга.
# Первый ход делает человек. 
# За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# # Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

from random import randint

count = 120
max_taken = 28
winner_hum = False
print('На столе лежит 120 конфет.')
print('В свой ход возьмите от 1 до 28 конфет включительно')
print('Победитель - тот, кто оставил на столе 0 конфет.', '\n')

while count != 0:
    win_step = count % (max_taken + 1)
    hum = int(input('Ваш ход: '))

    if hum <= 0 or hum > 28:
        print('Неверный ход, прочитайте условие еще раз', '\n')
        continue
    elif hum == win_step:
        count -= hum
        print('Осталось: ', count, '\n')
        if count == 0:
            winner_hum = True
            break
        bot = randint(1, 28)
    else:
        count -= hum
        print('Осталось: ', count, '\n')
        win_step = count % (max_taken + 1)
        bot = win_step

    print('Ход бота: ', bot)
    count -= bot
    print('Осталось: ', count, '\n')

print('Вы выиграли!' if winner_hum else 'Выиграл бот :(', '\n')
