dict = {
    1001: "varaliya",
    1002: "sahil",
    1003: "sameer",
    1004: "amaan"
}

print(dict[1001])
print(dict[1002])
print(dict[1003])
print(dict[1004])
print(type(dict))

# Python Dictionaries
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

# I. Accessing single values:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))

# II. Accessing multiple values:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

# III. Accessing keys:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

# IV. Accessing key-value pairs:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())



print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 