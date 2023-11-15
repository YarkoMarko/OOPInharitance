class Circle:
    def __init__(self):
        print("Circle")


class Square:
    def __init__(self):
        print("Square")


class CircleInSquare(Circle, Square):
    def __init__(self):
        super().__init__()
        Square.__init__(self)
        print("Circle in square")


c = CircleInSquare()