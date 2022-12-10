a = "!!! Varaliya !!!!!!!!"
print((len(a)))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))

print(a.replace("!", ""))

print(a.split(" "))

print(a.capitalize())

b = "hello WorlD"
print(b.capitalize())

c = "Welcome to the Console!!!"
print(c.center(50))
print(c.center(50, "."))

e = "Abracadabra"
print(e.count("a"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
print(str1.endswith("console"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.find("bxjkbjsa"))

str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())

str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())