import datetime


class Client:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.accounts = []


class Account:
    def __init__(self, holder, amount, date_created=None):
        self.holder = holder
        holder.accounts.append(self)
        self.amount = amount
        if date_created:
            self.date_created = date_created
        else:
            self.date_created = datetime.datetime.now()

    def __repr__(self):
        return "Account belonging to " + self.holder.name \
               + " created at " + self.date_created.isoformat() \
               + ". Amount: " + str(self.amount) + "PLN."

    def increase_amount(self, by_amount):
        self.amount += by_amount

    def decrease_amount(self, by_amount):
        if (self.amount - by_amount) < 0:
            print("niewystarczające środki")
        else:
            self.amount -= by_amount


jan = Client(name="Jan Nowak", phone_number="997997997")

accounts = [
    Account(
        holder=jan,
        amount=420,
        date_created=datetime.datetime(year=2019, month=10, day=1)
    ),
    Account(
        holder=Client(name="Janina Nowak", phone_number="420420420"),
        amount=1000,
        date_created=datetime.datetime(year=2020, month=9, day=1)
    ),
]

accounts.append(
    Account(
        holder=Client(name="Janiniusz Nowak", phone_number=""),
        amount=40
    )
)
print(accounts)

accounts.append(
    Account(
        holder=jan,
        amount=1000
    )
)
print(accounts)

jan.name = "Jan Mikołaj Nowak"

print(accounts)

print(jan.accounts)