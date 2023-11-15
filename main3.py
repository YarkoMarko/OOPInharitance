class Animal:
    _name = ""
    _type_of_animal = ""

    def sound(self):
        pass

    def show(self):
        print(f"Name: {self._name}")

    def type(self):
        print(f"Type: {self._type_of_animal}")


class Dog(Animal):
    def __init__(self, name):
        self._name = name
        self._type_of_animal = "Dog"

    def sound(self):
        print("Sound: Wolf!")


class Cat(Animal):
    def __init__(self, name):
        self._name = name
        self._type_of_animal = "Cat"

    def sound(self):
        print("Sound: Meow!")


class Parrot(Animal):
    def __init__(self, name):
        self._name = name
        self._type_of_animal = "Parrot"

    def sound(self):
        print("Sound: Kuku!")


class Hamster(Animal):
    def __init__(self, name):
        self._name = name
        self._type_of_animal = "Hamster"

    def sound(self):
        print("Sound: Ffffff!")


d = Dog("Ralf")
c = Cat("Rusty")
p = Parrot("Karl")
h = Hamster("Fatty")

d.sound()
d.type()
d.show()

c.sound()
c.type()
c.show()

p.sound()
p.type()
p.show()

h.sound()
h.type()
h.show()