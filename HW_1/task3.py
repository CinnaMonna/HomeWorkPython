# Task 3
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('input coordinate x: '))
y = int(input('input coordinate y: '))

if x > 0 and y > 0:
    print('this point is in the 1st quarter')
elif x < 0 and y > 0:
    print('this point is in the 2nd quarter')
elif x < 0 and y < 0:
    print('this point is in the 3d quarter')
elif x > 0 and y < 0:
    print('this point is in the 4th quarter')
else:
    print('the point is on the axis')


