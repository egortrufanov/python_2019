# 1
import time


class Ticket:

    def __init__(self, date, name, deadline):
        self.createDate = date
        self.owner = name
        self.deadline = deadline

    def __del__(self):
        print("Delete ticket: ", time.asctime(self.createDate))

    def display(self):
        print("Ticket:")
        print(" createDate: ", time.asctime(self.createDate))
        print(" owner: ", self.owner)
        print(" deadline: ", time.asctime(self.deadline))


# создание объект класса
ticket1 = Ticket(time.localtime(), "Ivan Ivanov", time.strptime("17.12.2017", "%d.%m.%Y"))
# вызов метода
ticket1.display()
# получение значения атрибута
print("Owner: ", ticket1.owner)
print("Owner(getattr): ", getattr(ticket1, "owner"))
# проверка наличия атрибута
print("hasattr: ", hasattr(ticket1, "owner"))
# установка значения атрибута
setattr(ticket1, "owner", "Alexei Petrov")
print("Owner(setattr): ", ticket1.owner)

# 2
# удаление значения атрибута
print("delattr: ", delattr(ticket1, "owner"))

# 3
# удаление объекта
del ticket1
print(ticket1)


# 4
class Time1:
    def __init__(self, date):
        self.Date = date

    def show(self):
        print("The time is", time.strftime("%d %b %Y %X", self.Date))


right_now = Time1(time.localtime())
right_now.show()


# 5
class Time:

    def __init__(self, date):
        self.Date = date

    def what_is_time(self):
        print("The time is", time.strptime(self.Date, "%d.%m.%Y %H:%M:%S"))


the_time = Time('17.07.2017 10:53:00')
the_time.what_is_time()
