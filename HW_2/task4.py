# Task 4
# Требуется посчитать сумму чётных чисел, расположенных 
# между числами 1 и N включительно

n = int(input('input N: '))
sum = 0
if n >= 0:
    for i in range(2, n + 1, 2):
        sum += i
else:
    if n % 2 == 0:
        for i in range(n, 1, 2):
            sum += i
    else:
        for i in range(n + 1, 1, 2):
            sum += i

print(f'''\nthe sum of even numbers located between 
the numbers 1 and {n} (incl.) is {sum}\n''')
