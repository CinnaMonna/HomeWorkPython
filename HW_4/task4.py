# Task 4
# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1

import randint_list

num_list = randint_list.random_list(8, 0, 6)
print('list of random natural numbers: \n', num_list)

repeats_set = set()
for num in num_list:
    if num_list.count(num) > 1:
        repeats_set.add(num)

new_num_list = []
for num in num_list:
    if num not in repeats_set:
        new_num_list.append(num)
print('list of non-repeating elements of the original list: \n', new_num_list)
    
