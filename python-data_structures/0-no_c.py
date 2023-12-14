def no_c(my_string):
    char_to_remove = ['c','C']
    result_string = ''.join([char for char in my_string if char not in char_to_remove])
    
    return result_string