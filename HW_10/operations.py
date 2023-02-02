def add_space(stroka):   
    if stroka[0] == '-':
        i = 1
    else:
        i = 0
    while i < len(stroka):
        if not stroka[i].isdigit() and stroka[i] != ' ' and stroka[i] != '.' :
            stroka = stroka[:i] + ' ' + stroka[i] + ' ' + stroka[i+1:]
            i += 2
        else:
            i += 1

    return stroka

def symb_to_res(spisok, sign):
    i = 1
    while i < len(spisok):
        if spisok[i] == sign:
            if sign == '/':
                res = float(spisok[i-1]) / float(spisok[i+1])
            elif sign == '*':
                res = float(spisok[i-1]) * float(spisok[i+1])
            elif sign == '-':
                res = float(spisok[i-1]) - float(spisok[i+1])
            elif sign == '+':
                res = float(spisok[i-1]) + float(spisok[i+1])
            del spisok[(i-1):(i+2)]
            spisok.insert(i-1, str(round(float(res), 2)))
            i = 1
        else:    
            i +=1  
  
    return spisok