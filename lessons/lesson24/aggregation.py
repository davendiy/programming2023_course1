
from abc import abstractmethod, ABC
from typing import List


class Figure(ABC):

    def __init__(self, safe=True) -> None:
        super().__init__()

        if safe:
            if not self.exists(): 
                raise ValueError('illegal parameters: figure doesnt exist')

    @abstractmethod
    def area(self):
        pass 

    @abstractmethod
    def perimeter(self): 
        pass 
    
    @abstractmethod
    def exists(self) -> bool: 
        pass 


class Rectangle(Figure):

    def __init__(self, a, b, safe=True) -> None:
        super().__init__(safe=safe)
        self.a = a
        self.b = b

    def area(self): 
        return self.a * self.b

    def perimeter(self):
        return self.a * 2 + self.b * 2

    def exists(self) -> bool:
        return True

    def __repr__(self): 
        return f'Rectangle({self.a}, {self.b})'


class Triangle(Figure): 

    def __init__(self, a, b, c) -> None:
        super().__init__()

        self.a = a 
        self.b = b 
        self.c = c


class Trapeze(Figure): 
    
    def __init__(self, a, b, c) -> None:
        super().__init__(safe=False)
        pass 


class Parallelogram(Figure): 
    pass 


class Circle(Figure): 
    pass


shapes = {
    "Rectangle": Rectangle, 
    "Triangle": Triangle, 
    "Trapeze": Trapeze, 
    "Parallelogram": Parallelogram,
    "Circle": Circle,
}


def figure_factory(line: str) -> Figure: 
    params = line.split() 
    name = params[0] 
    params = params[1: ]

    if name not in shapes: 
        raise ValueError(f'unknown name of figure: {name}')
    shape_type = shapes[name]
    
    res = shape_type(*params)     # type: Figure
    return res 


def find_max_area(figures: List[Figure]): 
    res = {Rectangle: 0, Trapeze: 0, Triangle: 0, Circle: 0, Parallelogram: 0}
    for el in figures: 
        cur_area = el.area()
        shape = type(el)
        if cur_area > res[shape]: 
            res[shape] = cur_area
    return res 
