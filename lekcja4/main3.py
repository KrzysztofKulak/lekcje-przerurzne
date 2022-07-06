def get_pi():
    return 3.14


def get_circle_circ(radius):
    return 2 * get_pi() * radius


def calculate_whole_thing(radius):
    return 3 * get_circle_circ(radius)

# print(get_circle_circ(4))
# print(get_circle_circ(14))
# print(get_circle_circ(12312412414))


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def is_decision_add(decision):
    if decision == "1":
        return True
    else:
        return False


def is_decision_subtract(decision):
    if decision == "2":
        return True
    else:
        return False


def calculate(decision, a, b):
    if is_decision_add(decision):
        return add(a, b)
    elif is_decision_subtract(decision):
        return subtract(a, b)
    else:
        return None


while True:
    users_decision = input("1 by dodawać, 2 by odejmować: ")
    if users_decision == "3":
        break
    first_value = int(input("podaj pierwszą wartość: "))
    second_value = int(input("podaj drugą wartość: "))

    print(calculate(users_decision, first_value, second_value))


# funkcja zawsze jest obiektem!!!!!!!11

# operations = {
#     "kalkulator": calculate
# }
#
# list_of_operations = [calculate, print]
#
# print(operations["kalkulator"]("2", 10, 12))