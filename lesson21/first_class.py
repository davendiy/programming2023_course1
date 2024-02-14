from math import sqrt
import matplotlib.pyplot as plt 


# NOT A METHOD 
def test_function(self): 
    pass 


class ComplexNumber: 

    def __init__(self, x, y): 
        """Create a complex number x + y*i.

        :param x: real part 
        :param y: imaginary part
        """
        
        # ATTRIBUTES
        self.x = x 
        self.y = y 

        # приклад як функцію можна зробити атрибутом. Але методом 
        # вона таким чином не стане (параметр self буде незаповнений)
        self.func = test_function
    
    # METHODS
    def norm(self): 
        return sqrt(self.x ** 2 + self.y ** 2)

    def real(self): 
        return self.x

    def imag(self): 
        return self.y

    def __repr__(self): 
        """Магічний метод, який викликається якщо __str__ не вказаний АБО коли об'єкт знаходиться в 
        якійсь іншій структурі (наприклад ви хочете вивести на екран список з комплексних чисел.)"""
        return f"ComplexNumber({self.x}, {self.y})"

    def __str__(self): 
        """Магічний метод, який викликається функцією str(). Наприклад при print."""
        return f"{self.x} + {self.y} * i"

    def __add__(self, other): 
        """Перевизначити додавання self + other (наш об'єкт стоїть зліва)."""
        if isinstance(other, int) or isinstance(other, float): 
            other = ComplexNumber(other, 0)
        
        if not isinstance(other, ComplexNumber): 
            raise TypeError(f"unsupported operation for ComplexNumber and {type(other)}")

        return ComplexNumber(
            self.x + other.x, 
            self.y + other.y
        )

    def __radd__(self, other): 
        """Перевизначити додавання other + self (потрібне коли до матриць додаємо число наприклад)"""
        return self.__add__(other)

    def __mul__(self, other): 
        """Те саме, тільки для множення."""
        if isinstance(other, int) or isinstance(other, float): 
            other = ComplexNumber(other, 0)
        
        if not isinstance(other, ComplexNumber): 
            raise TypeError(f"unsupported operation for ComplexNumber and {type(other)}")


        return ComplexNumber(
            self.x * other.x - self.y * other.y,
            self.y * other.x + self.x * other.y
        )

    def __rmul__(self, other): 
        return self * other 
        
    def __sub__(self, other):
        """Те саме, тільки для віднімання. Реалізовуємо його як додавання від'ємного. """
        return self + (other * (-1))

    def __abs__(self): 
        """Викликається функцією abs."""
        return self.norm()
        
    def draw(self, fig=None): 
        """Іграшковий приклад як можна комплексне число намалювати."""
        if fig is None: 
            fig = plt 

        fig.scatter([self.x], [self.y])

    def inverse(self): 
        """Рахує (1 / self)."""
        return self.conjugate() / self.norm() ** 2
       
    def conjugate(self):
        """Спряжений до комплексного числа, i.e. для a + bi виведе a - bi."""
        return ComplexNumber(self.x, -self.y)


# функції, а не методи. Функціями не можна перевизначити додавання через +
def add(z1: ComplexNumber, z2: ComplexNumber): 
    return ComplexNumber(
        z1.x + z2.x, 
        z1.y + z2.y
    )


def multiply(z1: ComplexNumber, z2: ComplexNumber): 

    return ComplexNumber(
        z1.x * z2.x - z1.y * z2.y,
        z1.y * z2.x + z1.x * z2.y
    )


# глобальна константа для легкого використання.
i = ComplexNumber(0, 1)


# create an object 
# test_number = ComplexNumber(2, 3)

# # print attributes
# print(test_number.x, test_number.y)
# print(test_number.func())


# # print methods 
# print(test_number.real(), test_number.imag())
# print(test_number.norm())
