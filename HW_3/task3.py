# Task 3
# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import input_float_list

def difference_fract_parts(user_list):
    fract = []
    for i in range(len(user_list)):
        if (user_list[i] - int(user_list[i])) != 0:
            fract.append(abs(user_list[i] - int(user_list[i])))
    
    # fract_max = fract[0]
    # for i in range(1, len(fract)):
    #     if fract[i] > fract_max:
    #         fract_max = fract[i]

    # fract_min = fract[0]
    # for i in range(1, len(fract)):
    #     if fract[i] < fract_min:
    #         fract_min = fract[i]

    # return(round(fract_max - fract_min, 2))

    return(round(max(fract) - min(fract), 2))
   

user_list = input_float_list.input_list()
print('difference of max and min fractional parts of numbers is: ', difference_fract_parts(user_list))
