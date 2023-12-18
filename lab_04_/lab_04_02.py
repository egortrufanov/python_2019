# 6

class Worker:
    'doc class Worker'
    count = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Worker.count += 1

    def display(self):
        print("Worker:")
        print("{} {}".format(self.name, self.surname))


w1 = Worker("Ivan", "Ivanov")
print("w1.count: ", w1.count)
w2 = Worker("Alexei", "Petrov")
print("w2.count: ", w2.count)
print("w1.count: ", w1.count)
print("Worker.count: {0} \n".format(Worker.count))
print("Worker.__name__: ", Worker.__name__)
print("Worker.__dict__: ", Worker.__dict__)
print("Worker.__doc__: ", Worker.__doc__)
print("Worker.__bases__: ", Worker.__bases__)


# 7
class Animal:
    'doc class Animal'
    id = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.id += 1

    def display(self):
        print("Animal id: ", Animal.id)
        print("Name: ", self.name)
        print("Age: ", self.age)


animal1 = Animal("Dog", 4)
animal2 = Animal("Cat", 12)
animal3 = Animal("Hamster", 1)
animal1.display()
animal2.display()
animal3.display()


# 8
# Из-за того, что определение значения атрибута id находится
# в методе для инициализации объекта класса, программа при каждом
# вводе нового объекта добавляет по единице в значение атрибута id,
# то есть после объявления всех объектов в атрибуте id будет
# хранится инфомация о количестве объектов в классе

# 9
class Animal:
    'doc class Animal'
    id = 0
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.count += 1

    def display(self):
        Animal.id += 1
        print("Animal id: ", Animal.id)
        print("Name: ", self.name)
        print("Age: ", self.age)


animal1 = Animal("Dog", 4)
animal2 = Animal("Cat", 12)
animal3 = Animal("Hamster", 1)
animal1.display()
animal2.display()
animal3.display()
