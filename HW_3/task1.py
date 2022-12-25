# Task 1
# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import input_int_list

def sum_val_odd_ind(user_list):
    sum = 0
    for i in range(1, len(user_list), 2):
        sum += user_list[i]
    
    return sum

user_list = input_int_list.input_list()
print('sum of values on odd indices is: ', sum_val_odd_ind(user_list))



