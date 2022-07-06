def say_hello():
    print("teraz wykonuję funkcję!")
    print("hello!")

say_hello()
print("hehe")
say_hello()

def say_hello_with_name(name):
    print("hello, " + name)

say_hello_with_name("Krzysiu")
say_hello_with_name("Szpadel")

def say_hello_with_name_n_times(name, n):
    for i in range(n):
        print("hello, " + name)

say_hello_with_name_n_times("Krzysiu", 5)

def add(a, b):
    return a + b
