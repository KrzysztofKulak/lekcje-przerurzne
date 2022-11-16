phrase = "wlazł kotek na płotek"
words = phrase.split("kotek")
print(len(phrase))
print(len(words))
print("średnia długość słowa to: " + str(len(phrase)/len(words)) + " i tyle")
print(f"średnia długość słowa to: {len(phrase)/len(words)} i tyle")


names_list = ["Piotr", "Paweł", "Gaweł"]
names = " mój ziomo ".join(names_list)
print(names)
