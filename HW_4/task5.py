# Task 5
#  Даны два файла, в каждом из которых находится запись многочлена. 
#  Задача - сформировать файл, содержащий сумму многочленов.

# решение только для многочленов, записанных в виде:
# ax^n + bx^(n-1) .... + cx^1 + dx^0  (с указанием степеней 1 и 0 и коэффициентов равных 1),
# с коэффициентами в интервале [0, 9] и старшей степенью не более 9

import pathlib
from pathlib import Path
dir_path = pathlib.Path.cwd()

path = Path(dir_path, 'HW_4', 'polynom1.txt')
with open(path, 'r') as data:
    for line in data:
        pol1_str = line

path = Path(dir_path, 'HW_4', 'polynom2.txt')
with open(path, 'r') as data:
    for line in data:
        pol2_str = line

def dict_coef(pol_str):
    dict_coef = {}
    for pow in range(0, 10):
        desired = 'x^' + str(pow)
        ind = pol_str.find(desired)
        if ind != -1:
            dict_coef[pow] = int(pol_str[ind - 1])
    return dict_coef

dict_coef1 = dict_coef(pol1_str)
dict_coef2 = dict_coef(pol2_str)

print('polynomial_1:\n', pol1_str)
print('power: coefficient\n', dict_coef1, '\n')
print('polynomial_2:\n',pol2_str)
print('power: coefficient\n', dict_coef2, '\n')



dict_coef_sum = {}
for key1 in dict_coef1.keys():
    for key2 in dict_coef2.keys():            
        dict_coef_sum[key1] = dict_coef1[key1]
        dict_coef_sum[key2] = dict_coef2[key2]

for key in dict_coef_sum:        
    if key in dict_coef1.keys() and key in dict_coef2.keys():
        dict_coef_sum[key] = (dict_coef1[key] + dict_coef2[key])

pol_sum_str = ''
for key in dict_coef_sum:
    pol_sum_str = str(dict_coef_sum[key]) + 'x^' + str(key) + ' + ' + pol_sum_str
pol_sum_str = pol_sum_str[:-3]

print('polynomial_sum = polynomial_1 + polynomial_2:\n', pol_sum_str)
print('power: coefficient\n', dict_coef_sum, '\n')


path = Path(dir_path, 'HW_4', 'sum_polynom.txt')
with open(path, 'w') as data:
    data.write(pol_sum_str)



