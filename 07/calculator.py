print("A Simple Calculator")

a = int(input("Enter first number : "))
b = int(input("Enter Second number : "))

c = input(f"Give operator to perform between {a} and {b} : ")


if (c == "+"):
    print(f"Addition of {a} and {b} is : ", a + b)

elif (c == "-"):
    print(f"Subtraction of {a} and {b} is : ", a - b)

elif (c == "*"):
    print(f"Multiplication of {a} and {b} is : ", a * b)

elif (c == "/"):
    print(f"Division of {a} and {b} is : ", a / b)

elif (c == "//"):
    print(f"Floor Division of {a} and {b} is : ", a // b)

elif (c == "%"):
    print(f"Modulus of {a} and {b} is : ", a % b)

elif (c == "**"):
    print(f"Exponential of {a} and {b} is : ", a ** b)

else:
    print("Invalid Input")

