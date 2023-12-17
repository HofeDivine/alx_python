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
        
    def area(self):
        square_area = self.__size**2
        return square_area
    def get_size(self):
        """
        a function to get the private instance size
        :return: The size of the square.
        """
        return self.__size
    def set_size(self,size):
        """
        a method that allows us to set a new size of our private instance of the class square
        :param size: The new size to set.
        """
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    