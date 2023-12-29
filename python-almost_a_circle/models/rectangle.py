"""
we are diving deep into python. This project is about python alnost a circle
"""
from models.base import Base
class Rectangle(Base):
    """
    this is a rectangle class that contains the private attributes
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        
        """
        this in the construstor of the base class
        it has id as an instance attributes
        """
        super().__init__(id)
        if not isinstance(width,int):
            raise TypeError("width must be an integer")
        self.__width = width
        if not isinstance(height,int):
            raise TypeError("height must be an integer")
        self.__height = height
        if not isinstance(x,int):
            raise TypeError("x must be an integer")
        self.__x = x
        if not isinstance(y,int):
            raise TypeError("y must be an integer")
        self.__y = y
    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
            
        else:
            self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
            
        else:
         self.__y = value
    
