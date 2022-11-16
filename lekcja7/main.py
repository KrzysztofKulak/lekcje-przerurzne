class Math:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


math = Math()

# print(math.add(1, 2))
# print(math.subtract(100, 20))


class Student:
    ma_wakacje = True

    def __init__(self, kierunek, imie, nazwisko, najebany=True):
        self.kierunek = kierunek
        self.imie = imie
        self.nazwisko = nazwisko
        self.najebany = najebany
        self.status_studenta = True

    def get_info(self):
        info = ""
        info += self.imie + " " + self.nazwisko
        if not self.status_studenta:
            info += " już nie"
        info += " studiuje " + self.kierunek + " i "
        if self.najebany:
            info += "jest najebany"
        else:
            info += "nie jest najebany"
        return info

    def toggle_najebany(self):
        self.najebany = not self.najebany

    def become_upierdolony(self):
        self.status_studenta = False
        self.toggle_najebany()


class Profesor:
    def upierdol(self, student):
        student.become_upierdolony()


student_0 = Student("informatyka", "Krzysiu", "Kułak")
print(student_0.get_info())
vetulani = Profesor()
vetulani.upierdol(student_0)
print(student_0.get_info())


student_1 = Student("filologia romańska", "Konrad", "Mongoł", False)
student_2 = Student("fizyka kwantowa", "Jakub", "Silny", True)
print(student_0.get_info())
print(student_1.get_info())
print(student_2.get_info())
student_1.toggle_najebany()
print(student_1.get_info())

# print(Student.ma_wakacje)
# print(student_0.ma_wakacje)
# Student.ma_wakacje = False
# print(Student.ma_wakacje)
# print(student_0.ma_wakacje)
# print(student_1.ma_wakacje)
# print(student_2.ma_wakacje)

print(type(1))
print(type(True))
print(type(student_0))