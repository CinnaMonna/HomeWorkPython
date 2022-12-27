# Task 1
# Пользователь вводит число, Вам необходимо вывести число Пи с той 
# точностью знаков после запятой, сколько указал пользователь(БЕЗ round())

import math

acc = int(input('enter the accuracy: '))
pi = int(math.pi * 10 ** acc) / 10 ** acc if acc != 0 else int(math.pi)

print(f'Pi with accuracy {acc} decimal', 'place' if acc == 1 else 'places', f'is {pi}')
