# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

lst = [i for i in input('Введите список элементов через пробел: \n').split()]
list_alpha = list(filter(lambda el: el.isalpha(), lst))
list_digit = list(filter(lambda el: el.isdigit(), lst))
list_alnum = list(filter(lambda el: el.isalnum() and not el.isalpha() and not el.isdigit(), lst))
list_other = list(filter(lambda el: not el.isalnum(), lst))

print('Элементы, состоящие только из букв: ', *list_alpha)
print('Элементы, состоящие только из цифр: ', *list_digit)
print('Элементы, состоящие из букв и цифр: ', *list_alnum)
print('Элементы, содержащие другие символы: ', *list_other, '\n')

