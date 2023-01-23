def output_data():
    path = 'HW_7\phonebook_1.txt'
    with open(path, 'r') as data:
        return(data.read())

def add_data_1(new_entry):
    path = 'HW_7\phonebook_1.txt'
    with open(path, 'a') as data:
        for el in new_entry:
            data.write(f'{el}\n')
        data.write('---------------\n')

def add_data_2(new_entry):
    path = 'HW_7\phonebook_2.txt'
    with open(path, 'a') as data:
        str = ''
        for i in range(len(new_entry)):
            str += new_entry[i]
            if i != len(new_entry) - 1:
                str += ', '
        data.write(f'{str}\n')
