student = {"name": "Krzysiu", "last_name": "Kułak"}

def print_student(student):
    print(student["name"], student["last_name"])

# print_student(student)


class Student:
    def __init__(self, name, last_name):
        print("STUDENT JEST TWORZONY!")
        self.name = name
        self.last_name = last_name
        self.enrollments = []

    def print_yourself(self):
        print(self.name, self.last_name)
        if self.enrollments:
            print("they are enrolled to: ")
            print(self.enrollments)

    def enroll(self, course):
        self.enrollments.append(course)

    def get_tuition(self, discount=0):
        total = 1400 * len(self.enrollments) - discount
        if total < 0:
            return 0
        else:
            return total

student_1 = Student("Krzysiu", "Kułak")
student_1.enroll("Math")
student_1.enroll("AP")
student_1.print_yourself()
print(student_1.get_tuition(200))
# print(student_1.name)
# print(student_1.last_name)

student_2 = Student("Jack", "Sparrow")
student_2.print_yourself()
print(student_2.get_tuition(500))


class Car:
    def __init__(self, make, year, distance_driven):
        self.make = make
        self.year = year
        self.distance_driven = distance_driven

    def run(self):
        print("brum brum")
        self.distance_driven += 10

car_1 = Car("BMW", 2009, 185000)
# print(car_1.make)
# print(car_1.distance_driven)
# car_1.run()
# print(car_1.distance_driven)
# car_1.distance_driven = 200000
# print(car_1.distance_driven)