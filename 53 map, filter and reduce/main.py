def cube(x):
    return x * x * x

print(cube(2))

# newl = []
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list general way
# for i in l:
#     newl.append(cube(i))

# print(newl)


# using map func
newl = list(map(lambda x: x*x*x, l))
print(newl)

# filter func
def filter_func(a):
    return a > 4

newnewl = list(filter(filter_func, l))
print(newnewl)
