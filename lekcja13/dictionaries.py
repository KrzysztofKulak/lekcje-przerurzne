
dog_list = ["Tali", 13, "śmierdziel"]
dog_dict = {
    "name": "Tali",
    "age": 13,
    "breed": "śmierdziel"
}

print(dog_dict["name"], dog_dict["age"], dog_dict["breed"])

for item in dog_dict.keys():
    print(item)

for item in dog_dict.values():
    print(item)


print(dog_dict.items())
for key, value in dog_dict.items():
    print(key, value)

dog_dict_2 = {
    "name": "Tali",
    "age": 14,
    "how_lovely_he_is": "Very much"
}

dog_dict.update(dog_dict_2)
print(dog_dict)
