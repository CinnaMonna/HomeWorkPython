from view import (view_data, 
                get_choice, 
                get_new_data as new, 
                incorrect_input as incorrect)

from model import (output_data as out, 
                add_data_1 as add_1, 
                add_data_2 as add_2)

from logger import logger


def process_data():
    choice = get_choice()
    while choice not in [1, 2]:
        incorrect()
        logger('-', 'incorrect input')
        choice = get_choice()
    
    if choice == 1:
        view_data(out())
        logger('all data', 'console output')
    else: 
        new_entry = new()
        add_1(new_entry)
        add_2(new_entry)
        logger(new_entry, 'new data input')






