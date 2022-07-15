tuple_a = (1, 2)
list_a = [1, 2, 3]
list_a[2] = 4
print(list_a)
# tuple_a[1] = 3 #  TO NIE ZADZIAŁA
# print(tuple_a)

set_a = {1, 2, 3}
print(set_a)
set_a.add(1)
set_a.add(4)
print(set_a)

list_a = [1, 2, 1, 2, 3, 4, 1, 2, 5]
dedup = list(set(list_a))
print(dedup)

dict_a = {}
# dict_a = dict()  # robi to samo, co powyżej

dict_b = {"imie": "Krzysiu", "nazwisko": "Kułak"}
print(dict_b["imie"])
dict_b["wiek"] = 27
print(dict_b)

def introduce_me(my_data):
    print("Nazywam się " + my_data["imie"] + " "
          + my_data["nazwisko"] + ", mam " + str(my_data["wiek"])
          + " lat.")

krzysiu_data = {"imie": "Krzysiu", "nazwisko": "Kułak", "wiek": 27}
mongou_data = {"imie": "Mongoł", "nazwisko": "Mongoliński", "wiek": 13}

# introduce_me(krzysiu_data)
# introduce_me(mongou_data)


def get_introduction_of_me_v2(name, surname, age):
    return ("Nazywam się " + name + " "
          + surname + ", mam " + str(age)
          + " lat.")


krzysiu_introduction = get_introduction_of_me_v2(krzysiu_data["imie"], krzysiu_data["nazwisko"], krzysiu_data["wiek"])
mongou_introduction = get_introduction_of_me_v2("Mon", "z rodu Gołów", 23)
mongou_introduction = get_introduction_of_me_v2("brzydko, chuj cie to obchodzi!!!!!", "Spadaj", "mam cię dość od")
print(krzysiu_introduction)
print(mongou_introduction)