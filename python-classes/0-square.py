class Square:
    """
    This is a square class with private instances
    :param size is the size of the square
    """
    def __init__(self,size):
        
         """
        Initializes a new Square instance with the given size.

        :param size: The size of the square.
        """
         self.__size = size
    def get__size(self,size):
         """
         a function to get the private instance size
         """
         return self.__size
    def set__size(self,size):
         """
         a metod that allows us to set a new size of our private instance of the class square
         """
         return self.__size

        
