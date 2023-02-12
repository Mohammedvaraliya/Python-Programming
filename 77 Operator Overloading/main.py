class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, self2):
        return Vector(self.i + self2.i, self.j + self2.j, self.k + self2.k)


v1 = Vector(3, 5, 6)
print(v1)

v2 = Vector(1, 4, 6)
print(v2)

print(v1 + v2)
print(type(v1 + v2))