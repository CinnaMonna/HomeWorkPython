# Task 3
# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. 
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

n = int(input('input integer number N: '))
list = []
if n >= 0:
    for i in range(-n, n + 1):
        list.append(i)
else:
    for i in range(n, -n + 1):
        list.append(i)
    list = list[::-1]

index_string = input(f'input 5 indices in range [0, {abs(2 * n)}], separated by a space:\n')
index_list = index_string.split( )
for i in range(len(index_list)):
    index_list[i] = int(index_list[i])

print()
print('list of values in range [-N, N]: \n', list)
print()
print('list of users indices: \n', index_list)
print()

mult = 1
for i in index_list:
    mult *= list[i]
    if i != index_list[4]:
       print(f'({list[i]})', end = ' * ') 
    else:
        print(f'({list[i]})', end = ' = ')
print(mult)

