class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="cat")
        self.breed = breed

    def make_sound(self):
        print("Meow")

    def cat_speciality(self):
        print("This cat can protect you with thief")




a = Animal("Animal", "AnimalMan")
a.make_sound()
print(a.name)
print(a.species)

d = Dog("Dog", "DoggerMan")
d.make_sound()
print(d.name)
print(d.breed)

c = Cat("Cat", "CatMan")
c.make_sound()
c.cat_speciality()
print(c.name)
print(c.breed)


