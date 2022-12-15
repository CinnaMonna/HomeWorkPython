# Task 1
# Напишите программу, которая принимает на вход цифру, обозначающую 
# день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

n = int(input('''Input the number of the day of the week 
    from 1 to 7:  '''))

if 0 < n < 6:
    print('no, it\'s not the weekend')
elif n == 6 or n == 7:
    print('yes, it\'s the weekend')
else:
    print('invalid number')
    


