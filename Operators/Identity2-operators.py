dict1 = {"name": "Nichada", "age": "20"}
dict2 = {"name": "Nichada", "age": "20"}
dict3 = dict1

print(dict1 is dict3)  # True

print(dict1 is dict2)  # False

print(dict1 == dict2)  # True
