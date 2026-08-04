class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_details(self):
        print(f"name = {self.__name:<15}, age = {self.__age}")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

# hold multiple Person class objects
persons = []

def get_person_details():
    name = input("enter name: ")
    age = int(input("enter age: "))

    # create a new Person class object
    person = Person(name, age)

    # add the person into persons collection
    persons.append(person)

def print_all_persons():
    print(f"| {'name':<15} | {'age':<5} |")
    for person in persons:
        print(f"| {person.get_name():<15} | {person.get_age():<5} |")

while True:
    print("your options are:")
    print(f"1. add a person's details")
    print(f"2. get all person details")
    print(f"3. exit")

    # get input from user
    option = int(input("enter your choice: "))

    # check the option
    if option == 1:
        get_person_details()
    elif option == 2:
        print_all_persons()
    elif option == 3:
        break
    else:
        print("invalid option detected, please try again")
    