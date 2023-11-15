class Employee:
    _name = ""
    _age = 0
    _wage = 0

    def Printer(self):
        print(f"Name: {self._name}\nAge: {self._age}\nWage: {self._wage}")


class President(Employee):
    def __init__(self, name, age, wage):
        self._name = name
        self._age = age
        self._wage = wage


class Manager(Employee):
    def __init__(self, name, age, wage):
        self._name = name
        self._age = age
        self._wage = wage


class Worker(Employee):
    def __init__(self, name, age, wage):
        self._name = name
        self._age = age
        self._wage = wage


p = President("asbfdhsa", 49, 12000)
m = Manager("nkhjnfd", 39, 6000)
w = Worker("qwebqjh", 40, 1200)

p.Printer()
m.Printer()
w.Printer()
