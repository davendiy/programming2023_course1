from math import sqrt 


class Point2d: 

    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y

    
class Vector2d: 

    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y 

    def scalar_prod(self, other): 
        if not isinstance(other, Vector2d): 
            raise ValueError(f"Can't find scalar product on {other}.")
        return self.x * other.x + self.y * other.y

    def norm(self): 
        return sqrt(self.scalar_prod(self))

    def __add__(self, other): 
        if isinstance(other, float) or isinstance(other, int): 
            return Vector2d(self.x + other, self.y + other)
        elif isinstance(other, Vector2d): 
            return Vector2d(self.x + other.x, self.y + other.y)
        else: 
            raise ValueError(f"Can't add object of type {type(other)} to vector.")

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int): 
            return Vector2d(self.x * other, self.y * other)
        raise ValueError(f"Can't multiply object of type {type(other)} to vector.")

    def is_colinear(self, other): 
        if isinstance(other, Vector2d): 
            return self.x * other.y == self.y * other.x


def create_vec(start: Point2d, end: Point2d): 
    return Vector2d(end.x - start.x, end.y - start.y)


class Plane2d: 

    def __init__(self, start: Point2d, direction: Vector2d):
        self.start = start
        self.dir = direction

    def is_online(self, point) -> bool: 
        if not isinstance(point, Point2d): 
            raise ValueError()
        aux = create_vec(self.start, point)
        return self.dir.is_colinear(aux)

    def is_paralel(self, other): 
        if isinstance(other, Vector2d): 
            return self.dir.is_colinear(other)
        elif isinstance(other, Plane2d): 
            return self.dir.is_colinear(other.dir)
        else: 
            raise ValueError()

    def intersection(self, other): 
        if not isinstance(other, Plane2d): 
            raise ValueError() 
        ...
