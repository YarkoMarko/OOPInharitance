class Doors:
    def __init__(self):
        print("Doors")


class Engine:
    def __init__(self):
        print("Engine")


class Wheels:
    def __init__(self):
        print("Wheels")


class Car(Doors, Engine, Wheels):
    def __init__(self):
        super().__init__()
        Engine.__init__(self)
        Wheels.__init__(self)
        print("Car")


c = Car()
