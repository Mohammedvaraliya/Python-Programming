class Vara:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is an {self.occ}")


a = Vara("varaliya", "Developer")
a.info()

b = Vara("DIvya", "HR")
b.info()

c = Vara()