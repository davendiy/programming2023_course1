from math import sqrt, asin, pi, cos, sin

try: 
    import matplotlib.pyplot as plt 
except ImportError: 
    import warnings
    warnings.warn("can't import matplotlib")
    plt = None 



class ComplexNumber(tuple): 
    """Один з варіантів як зробити клас незмінним -- наслідуватись 
    від кортежа. Нехай комплексне число -- це кортеж з двох елементів 
    (x, y). Нам потрібно, щоб при виклику ComplexNumber(x, y) такий 
    кортеж створювався, а self.x і self.y повертали нульовий і перший 
    елементи відповідно.
    
    Але у такому разі нам знадобиться інший метод конструктор
    замість __init__."""

    # ВАЖЛИВО: ми не можемо використати __slots__, якщо наслідуємся від кортежа
    # __slots__ = ['_r', '_phi']

    def __new__(cls, x, y):
        """Конструктор, який викликається перед __init__ і, власне, 
        створює обʼєкт, в той час як __init__ тільки додає атрибути. 
        
        Оскільки в кортежа нема атрибутів, нам доведеться перевизначити 
        саме метод __new__.""" 
        return super().__new__(cls, [x, y])

    def __init__(self, x, y): 
        """Ініціалізувати комплексне число x + y*i.

        Тут тільки додаємо наші атрибути _r, _phi суто як 
        кешування для тригонометричної форми. 

        Зауваження: це мало б сенс, якби тригонометрична форма рахувалась 
        довго і часто. В даному випадку це трохи натягнутий приклад і тільки 
        збільшує розмір класу. 

        :param x: real part 
        :param y: imaginary part
        """
        super().__init__()
        self._r = None 
        self._phi = None

    # Тепер атрибути self._x i self._y не існують, натомість 
    # нам треба власноруч діставати їх як нульовий і перший елементи 
    # кортежа відповідно.
    @property
    def x(self): 
        return self[0]

    @property
    def y(self): 
        return self[1]

    @classmethod
    def from_trigonometric(cls, r, phi):
        x = r * cos(phi)
        y = r * sin(phi)
        res = cls(x, y)
        res._r = r 
        res._phi = phi
    
    def norm(self): 
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def radius(self): 
        return self.norm()

    @property
    def r(self): 
        if self._r is None:        
            self._r = self.norm()
        return self._r

    @property
    def phi(self): 
        if self._phi is None: 
            self._phi = self.angle()
        return self._phi

    def angle(self): 
        if self == 0: 
            raise ValueError('unknown angle for zero number')
        
        if self.x > 0: 
            phi = asin(self.y / self.norm())
        else: 
            phi = pi - asin(self.y / self.norm())
        return phi 

    @property
    def real(self): 
        return self.x

    @property
    def imag(self): 
        return self.y

    def __repr__(self): 
        """Магічний метод, який викликається якщо __str__ не вказаний АБО коли об'єкт знаходиться в 
        якійсь іншій структурі (наприклад ви хочете вивести на екран список з комплексних чисел.)"""
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __str__(self): 
        """Магічний метод, який викликається функцією str(). Наприклад при print."""
        return f"{self.x} + {self.y} * i"

    @classmethod
    def _wrapper(cls, other): 
        if isinstance(other, int) or isinstance(other, float): 
            other = cls(other, 0)
        
        if not isinstance(other, cls): 
            raise TypeError(f"unsupported operation for {cls} and {type(other)}")
        return other

    def __add__(self, other): 
        """Перевизначити додавання self + other (наш об'єкт стоїть зліва)."""
        other = self._wrapper(other)
        return type(self)(
            self.x + other.x, 
            self.y + other.y
        )

    def __radd__(self, other): 
        """Перевизначити додавання other + self (потрібне коли до матриць додаємо число наприклад)"""
        return self.__add__(other)

    def __mul__(self, other): 
        """Те саме, тільки для множення."""
        other = self._wrapper(other)
        return type(self)(
            self.x * other.x - self.y * other.y,
            self.y * other.x + self.x * other.y
        )

    def __eq__(self, other): 
        other = self._wrapper(other)
        return self.x == other.x and self.y == other.y

    def __pow__(self, power):
        """Формула Муавра."""
        if not isinstance(power, int): 
            raise NotImplementedError()
        
        need = self

        if power == 0: 
            return type(self)(1, 0)
        elif power < 0: 
            need = need.inverse()
            power = -power

        r, phi = need.as_trigonometric()
        r = r ** power 
        phi = phi * power 
        return self.from_trigonometric(r, phi)

    # для використання комплексного числа як ключа в словнику
    def __hash__(self): 
        return super().__hash__()

    def __rmul__(self, other): 
        return self * other 

    def __sub__(self, other):
        """Те саме, тільки для віднімання. Реалізовуємо його як додавання від'ємного. """
        return self + (other * (-1))

    def __abs__(self): 
        """Викликається функцією abs."""
        return self.norm()

    def __truediv__(self, other): 
        other = self._wrapper(other)
        return self * other.inverse()

    def __rtruediv__(self, other): 
        return other * self.inverse()

    def draw(self, fig=None): 
        """Іграшковий приклад як можна комплексне число намалювати."""
        if fig is None: 
            fig = plt 

        fig.scatter([self.x], [self.y])

    def as_trigonometric(self): 
        """Повертає r, phi -- модуль і кут."""
        return self.r, self.phi

    def inverse(self): 
        """Рахує (1 / self)."""
        x, y = self.conjugate() 
        return type(self)(
            x / self.norm() ** 2, 
            y / self.norm() ** 2,
        )

    def conjugate(self):
        """Спряжений до комплексного числа, i.e. для a + bi виведе a - bi."""
        return type(self)(self.x, -self.y)


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


if __name__ == '__main__': 
    # create an object 
    test_number = ComplexNumber(2, 3)

    # print attributes
    print(test_number.x, test_number.y)
    # print(test_number.func())

    # # print methods 
    print(test_number.real, test_number.imag)
    print(test_number.norm())

    print(test_number / 10)

    print(test_number ** 10)


    test_dict = {test_number: 10}
    print(test_dict)

    print(ComplexNumber(2, 3) in test_dict)    # True 


    print(test_number.r)
    test_number._x = 10
    print(test_number.r)
    print(test_number.radius())

    print(ComplexNumber(2, 3) in test_dict)  # False
    print(test_number)

    import sys
    print(f'Розмір комплексного числа в байтах: {sys.getsizeof(test_number)}')
