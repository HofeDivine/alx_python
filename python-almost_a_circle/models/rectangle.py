"""
we are diving deep into python. This project is about python alnost a circle
"""
class Base:
    """
    this is base class haiving a private attributes __nb_objects
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        this in the construstor of the base class
        it has id as an instance attributes
        """
        self.id = id
        if id is not None:
           self.id = id 
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects

"""
this module contains a rectangle class with private instace attributes
"""
class Rectangle(Base):
    """
    this is a rectangle class that contains the private attributes
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        
        """
        this in the construstor of the base class
        it has id as an instance attributes
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
