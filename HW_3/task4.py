# Task 4
# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def dec_to_bin(number):
    bin_list = []
    while number != 0:
        remainder = number % 2
        bin_list.append(remainder)
        number = number // 2

    bin_list = bin_list[::-1]
    bin = str()
    for i in range(len(bin_list)):
        bin += str(bin_list[i])
    
    return(bin)

number = int(input('enter dec number: '))
print(f'{number} (dec) = {dec_to_bin(number)} (bin)')

