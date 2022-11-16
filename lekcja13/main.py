zmienna_0 = 123  # int
zmienna_1 = 1.23  # float
zmienna_2 = "abc"  # str
zmienna_3 = True  # bool
zmienna_4 = None  # NoneType

list_empty = []  # = list()
list_a = [zmienna_0, zmienna_1, zmienna_2, zmienna_3]
print(list_a)
list_a.append(zmienna_4)
print(list_a)

for zmienna in list_a:
    print(type(zmienna))

run = True
i = 0
while run:
    i += 1
    if i > 10:
        run = False
    else:
        print(f"i nie było większe od 10. i miało wartość {i}.")

# decision = input("Podaj decyzję: ")
# print(f"{decision}? Chujowa decyzja! xddd")

tuple_a = (1, 2, 3, 4, "abc")
tuple_b = (3,)
print(tuple_a[0])
# tuple_a[0] = "a"  NIE WOLNO

set_a = {1, 2, 3, 4, 1, 1, 1, 1, 2, 3, "abc"}
print(set_a)
set_a.add(1)
print(set_a)
set_a.remove(1)
print(set_a)
set_b = {4, 5, 6}
print(set_a.difference(set_b))
print(set_a.intersection(set_b))
print(2 in set_a)
