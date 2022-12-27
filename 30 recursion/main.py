# Factorial number recursion
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# Fibonacci number recursion
# 0
# 1
# 1
# 2
# 3
# 5
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))