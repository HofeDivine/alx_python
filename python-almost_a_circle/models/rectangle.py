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
    def get_width(self) :
        """
        this is the getter for the attribute width"""
        return self.__width 
    def get_height(self) :
        
        """
        this is the getter for the attribute height"""
        return self.__height 
    def get_x(self) :
        """
        this is the getter for the attribute x"""
        return self.__x 
    def get_y(self) :
        """
        this is the getter for the attribute y"""
        return self.__y 
    def set_width(self,width) :
        """this wis the setter for the attribute width"""
        self.__width = width 
    def set__height(self,height) :
        """this wis the setter for the attribute height"""
        self.__height = height
    def set_x(self,x) :
        
        """this wis the setter for the attribute x"""
        return self.__x 
    def set_y(self,y) :
        """this wis the setter for the attribute y"""
        self.__y = y 
    
