lista = []
lista.append(1)
lista.append("abc")

list_a = []
list_b = list()
list_c = [1, 2, 3, "abc"]
# list_c += lista
list_c.extend(lista)
print(list_c)
# del list_c[2]
list_c.remove('abc')
print(list_c)
print(list_c[1])
print(list_c[4])
print(list_c[-1])
print(list_c[-2])

# for element in list_c:
    # print("hehehe " + str(element))

list_d = [["pierwszy", "drugi", "trzeci"], 4]
print(list_d[0])
print(list_d[0][2])
