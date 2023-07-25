"""
We will implement:
__add__, __mult__

Addition:
    >>> v1 = Vector(2, 3)
    >>> v2 = Vector(4, 5)
    >>> v1 + v2
    Vector(6, 8)

Absolute::
    >>> v1 = Vector(4, 3)
    >>> abs(v1)
    5.0

Scalar multiplication::
    >>> v1 = Vector(1, 9)
    >>> v1 * 3
    Vector(3, 27)
"""
import math

class Vector:
    """Main class
        >>> v1 = Vector(1, 1)
    """
    
    def __init__(self,x=0,y=0):
        """Test
            >>> v1 = Vector(1, 9)

        Args:
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
        """
        self.x = x
        self.y = y
    
    def __repr__(self):
        """Representation
            >>> v1 = Vector(3, 4)
            >>> print(v1)
            Vector(3, 4)

        Returns:
            _type_: _description_
        """
        return f"Vector({self.x!r}, {self.y!r})"
    
    def __abs__(self):
        """Absolute value
            >>> v1 = Vector(3, 4)
            >>> abs(v1)
            5.0

        Returns:
            _type_: _description_
        """
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        """Boolean value
            >>> v1 = Vector(4, 3)
            >>> bool(v1)
            True

        Returns:
            _type_: _description_
        """
        return bool(abs(self))
    
    def __add__(self, other):
        """
        Addition:
            >>> v1 = Vector(2, 3)
            >>> v2 = Vector(4, 5)
            >>> v1 + v2
            Vector(6, 8)
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        """Scalar multiplication
            >>> v1 = Vector(1, 1)
            >>> v1 * 5
            Vector(5, 5)
            >>> abs(v1 * 2)
            4.0

        Args:
            scalar (_type_): _description_

        Returns:
            _type_: _description_
        """
        return Vector(self.x * scalar, self.y * scalar)               
    
vector = Vector(2,3)
print(vector)