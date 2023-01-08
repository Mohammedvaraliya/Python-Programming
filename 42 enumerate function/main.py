marks = [12, 3, 34, 443, 22, 223, 32, 4, 44, 556, 5]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Varaliya is a mighty programmer")
#     index += 1

# using enumerate function
for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Varaliya is a mighty programmer")

# using enumerate function start with 1
for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 3):
        print("Varaliya is a mighty programmer")