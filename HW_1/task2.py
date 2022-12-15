# (!!!Доп!!!) Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (0,0,0), (0,0,1) и тд.

x, y, z = 0, 0, 0
chek = not (x or y or z) == (not x) and (not y) and (not z)
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(f'({x}, {y}, {z}) - ', chek)


    


