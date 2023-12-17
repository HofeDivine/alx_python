"""
This module is about an area of a square
"""
class Square:
    """
    A class with a private variable as size
    """
    def __init__(self,size=0):
        """
        A constructor of Square class with size as private parameter
        :param size: an int type
        """
        self.__size = size
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        square_area = self.__size**2
        return square_area
