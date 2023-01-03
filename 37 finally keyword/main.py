# try:
#     a = [8, 4, 6, 5, 4, 3, 2, 3]
#     i = int(input("Enter a index number : "))
#     print(a[i])
# except:
#     print("Some error occured")
# finally:
#     print("I am always executed")



def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)


