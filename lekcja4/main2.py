def say_message_n_times(message, n):
    return message * n


message = input("Podaj wiadomość: ")
number_of_times = int(input("Podaj ile razy: "))

result = say_message_n_times(message, number_of_times)
print(result)

print(say_message_n_times("siema ", 3))


def get_pi():
    return 3.14

print(get_pi() + 3)

