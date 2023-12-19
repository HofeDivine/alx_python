class BaseGeometry:
    """
    BaseGeometry class with a public instance method area().
    """

    def area(self):
        """
        Public instance method that raises an Exception with the message
        "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates an integer value.
        Raises a TypeError if the value is not an integer.
        Raises a ValueError if the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <=0:
            raise ValueError("{} must be greater than 0".format(name))
class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
         
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height