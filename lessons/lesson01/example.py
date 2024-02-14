"""This is an example of a python program"""

# imports of some libraries
import numpy as np  


def test_function(x, y): 
    """An example of a function with documentation."""
    return x + y 


# class with some code as well
class TestClass: 

    def __init__(self): 
        self.x = 10 
        self.y = 20 

    def __str__(self): 
        return f"({self.x}, {self.y})"



if __name__ == "__main__": 
    print(test_function(2, 1))

