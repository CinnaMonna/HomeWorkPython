# Task 3
# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена 
# и вывести многочлен степени k.

from random import randint

def random_coef_list(size):
    coef_list = []
    for i in range(size):
        coef_list.append(randint(0, 100))   

    return coef_list


def polynom(power, coef_list):
    coef_list_rev = coef_list[::-1]
    polynom = str(coef_list_rev[0])
    for i in range(1, power + 1):
        if i == 1:
            polynom = str(coef_list_rev[i]) + 'x + ' + polynom
        else:
            polynom = str(coef_list_rev[i]) + 'x^' + str(i) + ' + ' + polynom  

    return polynom


pow = int(input('enter the highest power of polynomial: '))
coef_list = random_coef_list(pow + 1)
print('list of random coefficients:\n', coef_list)
print('polynomial:\n', polynom(pow, coef_list), '\n')
