with open('51 seek(), tell() and other functions\myfile.txt', 'r') as f:
    print(type(f))

    f.seek(10)

    print(f.tell())
    data = f.read(5)
    print(data)


with open('51 seek(), tell() and other functions\sample.txt', 'w') as f:
    f.write("Hello World!")
    f.truncate(5)

with open('51 seek(), tell() and other functions\sample.txt', 'r') as f:
    print(f.read())

