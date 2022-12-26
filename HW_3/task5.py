# Task 5
# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]

def negafibonacci(number):
    if number == -1:
        return 1
    elif number == -2:
        return -1
    else:
        return negafibonacci(number + 2) - negafibonacci(number + 1)

def fibonacci(number):
    if number == 0:
        return 0
    elif number in [1, 2]:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

n = int(input('enter natural number: '))
list_fibonacci = []
for num in range(-n, 0):
    list_fibonacci.append(negafibonacci(num))
for num in range(0, n + 1):
    list_fibonacci.append(fibonacci(num))

print('Negafibonacci & Fibonacci sequence:')
print(list_fibonacci)
