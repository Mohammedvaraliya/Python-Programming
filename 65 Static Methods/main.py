class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num += n

    @staticmethod
    def add(a, b):
        return a + b


result = Math.add(2, 6)
print(result)

a = Math(5)
print(a.addtonum(5))
print(a.num)


print(a.add(8, 9))