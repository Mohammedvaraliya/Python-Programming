a = 4
b = "4"

print(a is b)
print(a == b)

a = None
b = None

print(a is b) # exact location of object in memory
print(a is None) # exact location of object in memory
print(a == b) # value