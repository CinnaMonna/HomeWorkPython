from random import randint

def random_list(size, min, max):
    r_list = []
    for i in range(size):
        r_list.append(randint(min, max))   

    return r_list
