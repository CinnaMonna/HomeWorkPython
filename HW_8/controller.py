from view import get_role, incorrect_input, get_mode, get_lesson, get_surname, get_scores
from model import add_data, output_data
from lessons_db import path_list, lesson_num



def process_data():
    role = get_role()
    while role not in [1, 2]:
        incorrect_input()
        role = get_role()

    if role == 1: 
        teacher_actions()
    
    else:
        student_actions()

def teacher_actions():
    while True:
        mode = get_mode()
        if mode not in [0, 1]:
            incorrect_input()
            continue
        
        elif mode == 1:
            lesson = get_lesson()
            while lesson not in [0, 1, 2, 3, 4]:
                incorrect_input()
                lesson = get_lesson()

            path = path_list()
            add_data(path[lesson], get_surname(), get_scores())

        else:
            break

def student_actions():
    output_data(get_surname(), path_list())

    





        



            

        

