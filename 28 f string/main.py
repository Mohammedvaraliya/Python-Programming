# Old format
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Varaliya"

print(letter.format(name, country))

# Old format
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Varaliya"

print(letter.format(country, name))

# F string for latest version of python
print(f"Hey my name is {name} and I am from {country}")

# floting f string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.87594785678957645))


print(type(f"{2 * 30}"))