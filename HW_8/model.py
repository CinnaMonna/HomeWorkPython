from lessons_db import lesson_num

def add_data(path, surname, scores):
    with open(path, 'a') as data:
        data.write('')

    with open(path, 'r') as data:
        cur_data = data.read()
        data_list = cur_data.split('\n')
        
    flag = False
    check = surname.upper() + ' '
    for i in range(len(data_list)):
        if check in data_list[i]:
            data_list[i] += ' ' + scores
            flag = True
    if not flag:    
        data_list.append(check + scores)
    
    # print(data_list)

    with open(path, 'w') as data:
        new_data = '\n'.join(data_list)
        data.write(new_data)
    
    
def output_data(surname, path_list):

    flag = False
    check = surname.upper() + ' '
    for i in range(len(path_list)):
        with open(path_list[i], 'a') as data:
            data.write('')
        with open(path_list[i], 'r') as data:
            for line in data:
                if check in line:
                    print(lesson_num(i), ': ', line[len(check):])
                    flag = True
        
    if not flag:
        print('оценок еще нет')
                



        

        

