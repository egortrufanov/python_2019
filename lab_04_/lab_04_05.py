# 13
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def display(self):
        print(self.firstname, " ", self.lastname, " ,", self.age, " years")


class Student(Person):
    studentID = 0

    def __init__(self, recordBook):
        self.recordBook = recordBook

    def display(self):
        Student.studentID += 1
        print("Student's ID is", self.studentID)
        print("His recordbook concludes ", self.recordBook[0], " \'5\', ", self.recordBook[1], " \'4\', ",
              self.recordBook[2], " \'3\' and ", self.recordBook[3], " \'2\'", "\n")


student1 = Person("Andrey", "Andreev", 12)
student1.display()
recordBook = list(input("How much does that student has each of marks? ").split(" "))
student1 = Student(recordBook)
student1.display()

student2 = Person("Ivan", "Ivanov", 10)
student2.display()
recordBook = list(input("How much does that student has each of marks? ").split(" "))
student2 = Student(recordBook)
student2.display()

student3 = Person("Polina", "Petrova", 14)
student3.display()
recordBook = list(input("How much does that student has each of marks? ").split(" "))
student3 = Student(recordBook)
student3.display()


# 14
class Professor(Person):
    professorID = 0

    def __init__(self, degree):
        self.degree = degree

    def display(self):
        Professor.professorID += 1
        print("Professor's ID is", self.professorID)
        print("His degree is", self.degree, "\n")


professor1 = Person("Sergei", "Kortikov", 65)
professor1.display()
degree = input("What is degree of that professor? ")
professor1 = Professor(degree)
professor1.display()

professor2 = Person("Evgenii", "Antropov", 74)
professor2.display()
degree = input("What is degree of that professor? ")
professor2 = Professor(degree)
professor2.display()

professor3 = Person("Vasilii", "Vasil'ev", 30)
professor3.display()
degree = input("What is degree of that professor? ")
professor3 = Professor(degree)
professor3.display()
