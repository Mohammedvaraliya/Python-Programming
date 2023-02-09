class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])

    

e = Employee("Vara", 1000020)
print(e.name)
print(e.salary)

string = "Varaliya-1029019"
e1 = Employee(string.split("-")[0], string.split("-")[1])
print(e1.name)
print(e1.salary)

string2 = "john-108090"
e2 = Employee.fromStr(string2)
print(e2.name)
print(e2.salary)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

person = Person.from_string("John Doe, 30")
print(person.name, person.age)