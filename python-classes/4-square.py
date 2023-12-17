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
    @property
    def size(self):
        """
        A getter property to get the private instance size
        :return: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A setter property that allows us to set a new size of our private instance of the class square
        :param value: The new size to set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def my_print(self):
        """
        A method to print the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#"* self.__size)

