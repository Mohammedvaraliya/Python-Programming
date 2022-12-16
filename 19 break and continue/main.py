# for i in range(12):
#     if(i == 10):
#         break
#     print("5 X", i+1, "=", 5 * (i+1))

# print("Exitted from the loop")

for i in range(12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5 * (i))

print("Exitted from the loop")


i = 0
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):
    break