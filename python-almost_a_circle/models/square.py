"""
a class that inherits from a rectangle class
"""
from models.rectangle import Rectangle
class Square(Rectangle):
    """
    A square class that inherit from a rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        the constructor of the Square class having size, x,y and id as its instances
        """
        self.size = size
        super().__init__(size, size, x, y, id)
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,self.x,self.y,self.size)