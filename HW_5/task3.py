# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"

def rle(stroka):
    stroka_rle = ''
    k = 1
    for i in range(1, len(stroka)):
        if stroka[i - 1] == stroka[i]:
            k += 1
        else:
            stroka_rle += str(k) + stroka[i - 1]
            k = 1
    stroka_rle += str(k) + stroka[-1]
    
    return stroka_rle

def unrle(stroka_rle):
    stroka_unrle = ''
    for i in range(0, len(stroka_rle), 2):
        stroka_unrle += int(stroka_rle[i]) * stroka_rle[i + 1]
    return stroka_unrle

path = 'HW_5\stroka_to_RLE.txt'
with open(path, 'r') as data:
    for line in data:
        stroka = line

stroka1 = rle(stroka)
stroka2 = unrle(stroka1)
print(stroka, '\n', stroka1, '\n', stroka2, '\n')



