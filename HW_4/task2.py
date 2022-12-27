# Task 2
# Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.
# пример N = 12 Вывод: 2 * 2 * 3

def prime_divisors(number):
    
    div_list = []
    start = 2
    while number != 1:
        for divisor in range(start, number + 1):
            if number % divisor == 0:
                div_list.append(divisor)
                break
        number //= divisor
        start = divisor
    
    return div_list

n = int(input('enter natural number: '))
divisors = prime_divisors(n)

if len(divisors) > 1:
    print(f'prime divisors of a number {n} are: {divisors}')
    print(n, '= ', end = '')
    for val in divisors:
        print(val, '* ' if val != divisors[len(divisors) - 1] else '', end = '')
else:
    print(f'prime divisor of a number {n} is: {divisors}')

