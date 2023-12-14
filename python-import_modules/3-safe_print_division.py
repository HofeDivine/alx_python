def safe_print_division(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        return None
    else:
        print("Inside result: {}".format(result))
        return None
    finally:
        
        if 'result' in locals():
            print(" {}".format())
        
