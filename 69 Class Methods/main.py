class Employee:
    company = "Apple"
    name = "Vara"

    def show(self):
        print(f"The name is {self.name} and company name is {self.company}")

    @classmethod
    def changeCompany(self, newCompany):
        self.company = newCompany
        return self

emp = Employee()
emp.show()
emp.changeCompany("oooohooo")
emp.show()
print(emp.company)
