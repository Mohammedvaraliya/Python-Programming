class Person:
    name = "Vara"
    occupation = "Software Developer"
    networth = 100
    def info(self):
        print(f"{self.name} is an {self.occupation}.")


a = Person()
a.name = "Shubham"
a.occupation = "Accountant"
a.info()

b = Person()
b.name = "Nitika"
b.occupation = "HR"
b.info()

c = Person()
c.info()
