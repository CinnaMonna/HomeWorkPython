# Task 4
# Напишите программу, которая по заданному номеру четверти показывает 
# диапазон возможных координат точек в этой четверти (x и y).

quarter_num = int(input('input the number of plane\'s quarter: '))

if quarter_num == 1:
    print('x range: (0, +inf)')
    print('y range: (0, +inf)')
elif quarter_num == 2:
    print('x range: (-inf, 0)')
    print('y range: (0, +inf)')
elif quarter_num == 3:
    print('x range: (-inf, 0)')
    print('y range: (-inf, 0)')
elif quarter_num == 4:
    print('x range: (0, +inf)')
    print('y range: (-inf, 0)')
else:
    print('invalid number of quarter')

