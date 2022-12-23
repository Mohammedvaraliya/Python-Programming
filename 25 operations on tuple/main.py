country = ("Spain", "Italy", "India", "England" "Germany")
print(country)

tmp = list(country)
tmp.append("Russia")
tmp.pop(3)
tmp[2] = "Finland"
print(tmp)

countries = tuple(tmp)
print(countries)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# count() Method
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

# Index method
Tuple = (0, 1, 2, 31, 2, 3, 1, 3, 2)
res = Tuple.index(31)
print('First occurrence of 3 is', res)

# Index method
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3, 4, 8)
print('First occurrence of 3 is', res)

# length method
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = len(Tuple)
print('Length of tuple is ', res)