print("podaj mi liczby całkowite")
while True:
    decision = int(input("napisz 1, by mnożyć, napisz 2, by dodawać: "))
    a = int(input("pierwszą:"))
    b = int(input("drugą:"))
    if decision == 1:
        print("wynik mnożenia twoich liczb to:")
        print(a * b)
    elif decision == 2:
        print("wynik dodawania twoich liczb to:")
        print(a + b)
    elif decision == 3:
        print("wynik dzielenia twoich liczb to: " + str(a / b))
    elif decision == 4:
        print("wynik odejmowania twoich liczb to:")
        print(a - b)
    else:
        break
print("do widzenia hehe")
