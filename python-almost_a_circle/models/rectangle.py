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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    def get__width(self) :
        """
        this is the getter for the attribute width"""
        return self.__width 
    def get__height(self) :
        
        """
        this is the getter for the attribute height"""
        return self.__height 
    def get__x(self) :
        """
        this is the getter for the attribute x"""
        return self.__x 
    def get__y(self) :
        """
        this is the getter for the attribute y"""
        return self.__y 
    def set__width(self) :
        """this wis the setter for the attribute width"""
        return self.__width 
    def set__height(self) :
        """this wis the setter for the attribute height"""
        return self.__height 
    def set__x(self) :
        
        """this wis the setter for the attribute x"""
        return self.__x 
    def set__y(self) :
        """this wis the setter for the attribute y"""
        return self.__y 
    
