
import random

HORIZONT = 0
VERTICAL = 1

class Object:

    def __init__(self, position) -> None:
        self.position = position

    def get_body(self):
        pass

    def get_area(self):
        pass


class Ship(Object):

    def __init__(self, position: tuple, orient: int, size: int) -> None:
        super().__init__(position)
        self.size = size
        self.orient = orient

    def get_body(self):
        if self.orient == VERTICAL:
            for i in range(self.size):
                yield self.position[0] + i, self.position[1]
        else:
            for i in range(self.size):
                yield self.position[0], self.position[1] + i

    def get_area(self):
        if self.orient == VERTICAL:
            x1, x2 = self.position[0] - 1, self.position[0] + self.size + 1
            y1, y2 = self.position[1] - 1, self.position[1] + 2
        else:
            x1, x2 = self.position[0] - 1, self.position[0] + 2
            y1, y2 = self.position[1] - 1, self.position[1] + self.size + 1

        for x in range(x1, x2):
            for y in range(y1, y2):
                yield (x, y)

    @classmethod
    def generate(cls, shape: tuple, size):
        max_x, max_y = shape
        x, y = random.randrange(max_x), random.randrange(max_y)
        orient = random.choice([HORIZONT, VERTICAL])
        return cls((x,y), orient=orient, size=size)

    def __repr__(self) -> str:
        return 'Ship'


# todo:
class Mine(Object):
    pass


class Map:

    config = {
        'ships': {
            1: 4,
            2: 3,
            3: 2,
            4: 1
        }
    }

    def __init__(self, shape) -> None:
        self.shape = shape
        self._list_objects = []
        self._objects = [[None] * self.shape[1] for _ in range(self.shape[0])]
        self._misses = [[0] * self.shape[1] for _ in range(self.shape[0])]
        self._areas = [[None] * self.shape[1] for _ in range(self.shape[0])]
        self._occupied = [[0] * self.shape[1] for _ in range(self.shape[0])]

    def add_ship(self, ship: Ship):
        for x, y in ship.get_body():
            if x < 0 or x >= self.shape[0]:
                raise ValueError()
            if y < 0 or y >= self.shape[1]:
                raise ValueError()
        for x, y in ship.get_area():
            if 0 <= x < self.shape[0] and 0 <= y < self.shape[1] and self._occupied[x][y]:
                raise ValueError()

        self._add_object(ship, area_occupied=True)

    def add_mine(self, mine: Mine):
        pass

    def _add_object(self, obj: Object, area_occupied=False):
        for x, y in obj.get_body():
            self._occupied[x][y] = 1
            self._objects[x][y] = obj
        for x,y in obj.get_area():
            if area_occupied:
                if x < 0 or x >= self.shape[0]: continue
                if y < 0 or y >= self.shape[1]: continue
                self._occupied[x][y] = 1
            self._areas[x][y] = obj
        self._list_objects.append(obj)

    @classmethod
    def generate(cls, shape, max_tries=10):
        res = cls(shape)

        # todo: not optimal generation
        for size, amount in cls.config['ships'].items():
            for _ in range(amount):
                for _ in range(max_tries):
                    try:
                        ship = Ship.generate(shape, size)
                        res.add_ship(ship)
                        break
                    except ValueError:
                        continue
                else:
                    raise ValueError("Couldn't generate map.")
        return res

    def show(self):
        res = [[' '] * self.shape[1] for _ in range(self.shape[0])]

        for obj in self._list_objects:
            for (x, y) in obj.get_area():
                if 0 <= x < self.shape[0] and 0 <= y < self.shape[1]:
                    res[x][y] = '.'

            for (x, y) in obj.get_body():
                res[x][y] = 'x'

        print('-' * (self.shape[0] * 2 + 3))
        for row in res:
            print('|', *row, '|')
        print('-' * (self.shape[0] * 2 + 3))


# todo:
class Player:
    pass


if __name__ == '__main__':

    field = [[' '] * 10 for _ in range(10)]

    x = Ship((2, 3), VERTICAL, size=4)
    for i, j in x.get_area():
        field[i][j] = '.'
    for i, j in x.get_body():
        field[i][j] = 'x'

    for row in field:
        print(*row)

    field = [[' '] * 10 for _ in range(10)]

    x = Ship((2, 3), HORIZONT, size=4)
    for i, j in x.get_area():
        field[i][j] = '.'
    for i, j in x.get_body():
        field[i][j] = 'x'

    for row in field:
        print(*row)


    # map = Map(shape=(3, 3))
    # map.add_ship(x)

    # for row in map._occupied:
    #     print(*row)

    # print()
    # for row in map._objects:
    #     print(*row)

    test_map = Map.generate(shape=(15, 15))
    test_map.show()
