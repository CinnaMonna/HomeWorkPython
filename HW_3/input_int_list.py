def input_list():
    user_values = input('enter the elements of the list separated by a space:\n')
    user_list = user_values.split( )
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])
    
    return(user_list)