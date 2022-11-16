student_0 = {
    "name": "Baltazar Gompka",
    "age": 14,
    "courses": ["math", "english"]
}

def generate_student_dict(name, age, courses):
    return {
        "name": name,
        "age": age,
        "courses": courses
    }

student_1 = generate_student_dict("John Doe", 12, ["PE"])

print(student_1)

student_2 = generate_student_dict("Baltazara Gompka", 16, ["Polish", "English", "Math"])

students = [student_1, student_2, generate_student_dict("Max", 10, ["Art"])]
print(students[2]["courses"])
print(students)

# OLD VERSION
# def get_courses(courses):
#     courses_list = ""
#     for course in courses:
#         courses_list += course + " "
#     return courses_list

def get_courses(courses):
    return ", ".join(courses)


def does_discount_apply_to_student(student):
    return len(student["courses"]) > 2 or student["age"] < 12


for student in students:
    print(student["name"] +
          " uczy się kursów: " +
          get_courses(student["courses"])
          )
    if does_discount_apply_to_student(student):
        print("studentowi należy się zniżka")

# print(", ".join(students[1]["courses"]))
