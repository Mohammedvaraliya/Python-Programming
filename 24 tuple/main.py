# tup = (1, 6, 7, 7)
# print(type(tup), tup)

tup = (1)
print(type(tup), tup)

tup = (1, )
print(type(tup), tup)

tup = (1, 98, 87, 65, 45, 78, 34)
print(tup[0])
print(tup[2])
print(tup[3])
# tup[0] = 100 # TypeError: 'tuple' object does not support item assignment

tup = (1, 98, 87, 65, 45, 78, 34, "green")
print(tup)

tup = (1, 98, 87, 65, 45, 78, 34, "green", "blue")
print(tup[-1])
 
if "green" in tup:
    print("yes its present")

# slicing
tup2 = tup[::-1]
print(tup2)