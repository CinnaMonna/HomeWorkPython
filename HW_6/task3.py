# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


def sum_nums(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum

lst = list(input('введите вещественное число: '))
lst = list(filter(lambda symb: symb.isdigit(), lst))
lst = list(map(int, lst))

print('сумма цифр в числе: ', sum_nums(lst), '\n')



