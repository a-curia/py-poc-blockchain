name = "Gogu"
age = "36"


def print_data():
    print(name + " " + age)


def print_data_args(name, age):
    print(name + " - " + str(age))


print_data()
print_data_args("GoguDemagogu", 36)


def print_decades(age):
    print("You lived {} decades".format(str(age // 10)))


print_decades(36)
