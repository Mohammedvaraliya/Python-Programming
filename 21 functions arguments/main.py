# The Functions
def average(a, b):
    print("The average is :" , (a+b)/2)

average(4, 6)

# Function with default arguments
def average(a=1, b=3):
    print("The average is :" , (a+b)/2)

average()

# Function with default arguments, but if we want to change one argument, we can
def average(a=1, b=3):
    print("The average is :" , (a+b)/2)

average(4)

# Function with default arguments, but if we want to change one argument, we can
# Here b argument changes
def average(a=1, b=3):
    print("The average is :" , (a+b)/2)

average(b=4)

# Default arguments:
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")

# Arbitrary Arguments:
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum/(len(numbers)))

average(3, 4, 5, 6, 3, 5, 2, 5, 1, 3, 6)

# Keyword Arbitrary Arguments:
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

# return Statement
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))