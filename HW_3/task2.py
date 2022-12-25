# Task 2
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math

def product_pairs(user_list):
    product = []
    for i in range(math.ceil(len(user_list) / 2)):
        product.append(user_list[i] * user_list[-i - 1])
    return product

user_values = input('enter the elements of the list separated by a space:\n')
user_list = user_values.split( )
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

print('products of pairs of numbers are: ',product_pairs(user_list))

