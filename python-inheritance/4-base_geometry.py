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