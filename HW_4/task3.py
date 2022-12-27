# Task 3
# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена 
# и вывести многочлен степени k.

import randint_list

def polynom(power, coef_list):
    coef_list_rev = coef_list[::-1]
    polynom = str(coef_list_rev[1]) + 'x + ' + str(coef_list_rev[0])
    for i in range(2, power + 1):
        polynom = str(coef_list_rev[i]) + 'x^' + str(i) + ' + ' + polynom  

    return polynom

pow = int(input('enter the highest power of polynomial: '))
coef_list = randint_list.random_list(pow + 1, 0, 100)
print('list of random coefficients:\n', coef_list)
print('polynomial:\n', polynom(pow, coef_list), '\n')
