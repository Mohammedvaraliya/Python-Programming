marks = [3, 5, 6, "varaliya", True, 9, 9, 7, 6, 5]
# print(marks)
# print(type(marks))

# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])

print(marks[-3]) # Negative Index
print(marks[len(marks)-3]) # Positive index
print(marks[5-3]) # Positive index
print(marks[2]) # Positive index

# To know element in present or not
if "varaliya" in marks:
    print("Yes")
else:
    print("No")

# To know element in present or not
if "liya" in "varaliya":
    print("Yes")
else:
    print("No")

# To print all the elements from list
print(marks[:])

# To print the element from
print(marks[0:3]) 

# To print the element with jump index
print(marks[0:6:2]) 

# List comprehension
lst = [i*i for i in range(8)]
print(lst)
lst = [i*i for i in range(8) if (i % 2 == 0)]
print(lst)