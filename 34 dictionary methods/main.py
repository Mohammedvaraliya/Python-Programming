# Update method
employee_performance_1 = {
    122: 45,
    123: 98,
    124: 89,
    125: 49
}

employee_performance_2 = {
    222: 70,
    223: 75,
    224: 82,
    225: 90
}

employee_performance_1.update(employee_performance_2)
print(employee_performance_1)

# Clear() method
employee_performance_1 = {
    122: 45,
    123: 98,
    124: 89,
    125: 49
}
employee_performance_1.clear()
print(employee_performance_1)

# To make emplty dictionary
emp = {}
print(type(emp))

# pop method
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

# popitem method
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003, 'gender': "Male"}
info.popitem()
print(info)

# del method
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info) #error
