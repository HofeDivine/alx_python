"""
 function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
"""
def inherits_from(obj, a_class):
    """
     function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
    """
    if type(obj) is a_class:
        return False
    for base in type(obj).__bases__:
        if base is a_class or inherits_from(base,a_class):
            return True
        return False