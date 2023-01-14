a = 6 # global variable
print(a)

def hello():
    a = 5 # local variable
    print(f"The local a is {a}")


print(f"The global a is {a}")
hello()
print(f"The global a is {a}")
print("\n")

# To change the global variable from function
a = 6 # global variable
print(a)

def hello():
    global a
    a = 5
    print(f"The local a is {a}")


print(f"The global a is {a}")
hello()
print(f"The global a is {a}")

