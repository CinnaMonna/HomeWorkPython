# Task 2
# Требуется найти наименьший натуральный делитель целого числа N, 
# отличный от 1.
# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

n = int(input('input integer number: '))

if n == 1:
    print('there is no natural divisor, not equal to 1')
else:
    if n == 0:
        divisor = 2
    else:
        for divisor in range(2, abs(n) + 1):
            if n % divisor == 0:
                break
    print('minimal natural divisor, not equal to 1, is: ', divisor)
