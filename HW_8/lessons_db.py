def path_list():
    path_list = ['HW_8\math.txt',\
                 r'HW_8\russ.txt',\
                 'HW_8\liter.txt',\
                 r'HW_8\biol.txt',\
                 'HW_8\geogr.txt']
    return(path_list)

def lesson_num(num):
    lesson_dict = {0:'Math', 1:'Russian', 2:'Literature', 3:'Biology', 4:'Geografy'}
    return lesson_dict[num]
