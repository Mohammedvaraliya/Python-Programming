# Reading a file
f = open('49 file IO\myfile.txt', 'r')
text = f.read()
print(text)
f.close()

# writing to a file
f = open('49 file IO\myfile2.txt', 'w')
f.write('Hello, world!')
f.close()

# Append to a file
f = open('49 file IO\myfile2.txt', 'a')
f.write('Hello, world!')
f.close()

# with open
with open('49 file IO\myfile.txt', 'w') as f:
    f.write('how r u changed to i am good')

# with open
with open('49 file IO\myfile.txt', 'r') as f:
    text = f.read()
    print(text)


