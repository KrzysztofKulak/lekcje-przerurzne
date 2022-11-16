dogs = []

class Owner:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Dog:
    def __init__(self, name, breed, age, owner):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner = owner

    def __str__(self):
        return f"{self.breed} {self.name}, {self.age} lat"



decision = None
while decision != 3:
    if dogs:
        print("Mamy psy:")
        for i, dog in enumerate(dogs):
            print(f"{i + 1}. {dog}")
        print('\n')
    print("1. Dodaj psa")
    print("2. Usuń psa")
    print("3. Wyjdź")
    decision = int(input())
    if decision == 1:
        name = input("Podaj imię psa: ")
        breed = input("Podaj rasę psa: ")
        age = input("Podaj wiek psa: ")
        dogs.append(Dog(name, breed, age, None))
    elif decision == 2:
        name = input("Podaj imię psa do usunięcia: ")
        for dog in dogs:
            if dog.name == name:
                dogs.remove(dog)
        else:
            print("Nie znaleziono psa o podanym imieniu")


































