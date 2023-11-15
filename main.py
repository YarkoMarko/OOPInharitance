class Square:
    def __init__(self):
        self._side = int(input("Enter side of square: "))


class Circle:
    _radius = 0


class CircleInSquare(Square, Circle):
    def __init__(self):
        super().__init__()
        Circle.__init__(self)
        self._radius = self._side / 2
        print(3.14 * (self._radius ** 2))


c = CircleInSquare()