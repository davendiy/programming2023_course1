from math import sqrt 

eps = 1e-5


def _determinant(matrix): 
    return (
        matrix[0][0] * matrix[1][1] 
        - matrix[0][1] * matrix[1][0]
    )


def _inverse2x2(matrix): 
    
    minors = [
        [matrix[1][1], -matrix[1][0]], 
        [-matrix[0][1], matrix[0][0]]
    ]

    det = _determinant(matrix)
    if abs(det) < eps: 
        raise ValueError('singular matrix')
    
    return [
        [minors[0][0] / det, minors[0][1] / det], 
        [minors[1][0] / det, minors[1][1] / det]
    ]


class Point2d: 

    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y

    def __repr__(self): 
        return f'Point2d({self.x}, {self.y})'

    
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
            return abs(self.x * other.y - self.y * other.x) < eps


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

        if self.is_paralel(other): 
            raise ValueError()
        
        u1, v1 = self.dir.x, self.dir.y 
        u2, v2 = other.dir.x, other.dir.y 
        x1, y1 = self.start.x, self.start.y 
        x2, y2 = other.start.x, other.start.y

        matrix = [[v1, -u1], [v2, -u2]]
        inv = _inverse2x2(matrix)
        vec = [v1 * x1 - u1 * y1, v2 * x2 - u2 * y2]

        x = inv[0][0] * vec[0] + inv[0][1] * vec[1]
        y = inv[1][0] * vec[0] + inv[1][1] * vec[1]

        res = Point2d(x, y)
        print(res)
        assert self.is_online(res)
        assert other.is_online(res)
        return res 


if __name__ == '__main__': 

    print(_inverse2x2([[1, 0], [0, 1]]))
    print(_inverse2x2([[0, -1], [2, 3]]))

    line1 = Plane2d(Point2d(1, 1), Vector2d(2, 3))
    line2 = Plane2d(Point2d(-2, 5), Vector2d(2, -3))

    print("is paralel:", line1.is_paralel(line2))
    print("intersection:", line1.intersection(line2))
