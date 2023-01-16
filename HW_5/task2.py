# 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

field = ''' 1 | 2 | 3 
----------
 4 | 5 | 6
----------
 7 | 8 | 9'''
print(field)

count_steps = 0
winner_x = False
winner_0 = False

while count_steps < 9:
    num_x = input('Номер поля для Х: ')

    if num_x in field:
        i = field.index(num_x)
        field = field[:i] + 'X' + field[(i + 1):]
        print(field)
        count_steps += 1
    else:
        print("введите номер свободного поля (от 1 до 9)")

    if field[1] == field[5] == field[9] == 'X' or\
       field[24] == field[28] == field[32] == 'X' or\
       field[46] == field[50] == field[54] == 'X' or\
       field[1] == field[24] == field[46] == 'X' or\
       field[5] == field[28] == field[50] == 'X' or\
       field[9] == field[32] == field[54] == 'X' or\
       field[1] == field[28] == field[54] == 'X' or\
       field[9] == field[28] == field[46] == 'X':
        winner_x = True
        break

    if count_steps == 9:
        break

    num_0 = input('Номер поля для 0: ')

    if num_0 in field:
        i = field.index(num_0)
        field = field[:i] + '0' + field[(i + 1):]
        print(field)
        count_steps += 1
    else:
        print("введите номер свободного поля (от 1 до 9)")
    
    if field[1] == field[5] == field[9] == '0' or\
       field[24] == field[28] == field[32] == '0' or\
       field[46] == field[50] == field[54] == '0' or\
       field[1] == field[24] == field[46] == '0' or\
       field[5] == field[28] == field[50] == '0' or\
       field[9] == field[32] == field[54] == '0' or\
       field[1] == field[28] == field[54] == '0' or\
       field[9] == field[28] == field[46] == '0':
        winner_0 = True
        break

    
if not winner_x and not winner_0:
    print('Ничья', '\n')
else:
    print('Победил играющий за', 'крестики' if winner_x else 'нолики', '\n')