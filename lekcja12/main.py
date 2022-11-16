from collections import namedtuple

list_a = ["123", 123, "abc", True, None]

for i, item in enumerate(list_a, start=1):
    print(f"{i}. {item}")

print(id(list_a))
list_a += [1, 2]
print(id(list_a))
tuple_a = (1, None, 3, "abc", 5)
print(id(tuple_a))
tuple_b = tuple_a + (1, 2, 3)
print(id(tuple_a))
print(type(tuple_a))
tuple_c = (123, "abc")
number, letters = tuple_c
print(number)
print(letters)

name, last_name, age = "Jan", "Kowalski", 12

a = 14
b = 10
a, b = b, a
print(a, b)

def func_a():
    return 12, "a"

a, b = func_a()
print(a, b)

Person = namedtuple("Person", ("elo", "melo"))
person = Person(elo="abc", melo=123)
print(person.melo)
print(person.elo)
print([person])

def func_a(a, b, c):
    return a + b + c


def func_b(a, b, c):
    return a * b * c


def func_c(a, b, c):
    return a - b - c


func_tuple = (func_a, func_b, func_c)

for func in func_tuple:
    print(func(2, 3, 5))


print(type(func_a))

function_hehe = func_a
print(function_hehe(1, 2, 4))

def func_a(a):
    print(a + "!")

def func_b(a):
    print(a + " :(")

def func_c(a):
    print(a + " : |")

reaction_map = {
    "kolega": func_a,
    "wróg": func_b,
    "człowiek": func_c
}

koledzy = ["fajny kolega", "super kolega", "chujowy wróg", "zwykły człowiek"]

for kolega in koledzy:
    reaction_map[kolega.split(" ")[1]](kolega)

print(koledzy[0].split(" ")[0][2])

map()