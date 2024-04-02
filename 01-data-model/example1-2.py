"""
A Vector class with special methods.

The methods included are:
``__repr__``, ``__add__``, ``__abs__``, ``__sub__``, and ``__mul__``

``__repr__``
>>> v = Vector(-1, 2)
>>> v
Vector(-1, 2)

``__add__``
>>> v1 = Vector(2, 5)
>>> v2 = Vector(-3, -1)
>>> v1 + v2
Vector(-1, 4)

``__abs__``
>>> v = Vector(3, 4)
>>> abs(v)
5.0

``__sub__``
>>> v1 = Vector(2, 5)
>>> v2 = Vector(-3, -1)
>>> v1 - v2
Vector(5, 6)

``__mul__``
>>> v = Vector(3, 4)
>>> v*2
Vector(6, 8)


"""
import math

class Vector:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()