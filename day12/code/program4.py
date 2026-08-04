# define a person class to store person details
# - name, address, age, phone, email

class Person:
    # default initializer
    def __init__(self):
        print(f"__init__() is called for self = {self}") 

        # add all instance properties
        self.name = "person1"
        self.address = "pune"
        self.age = 40
        self.phone = "+9123423424"
        self.email = "person1@test.com"


# create a referenced object of Person class
# person1 becomes self when the initializer gets called
person1 = Person()
print(f"person1 = {person1}")
print(f"name = {person1.name}")
print(f"address = {person1.address}")
print(f"age = {person1.age}")
print(f"phone = {person1.phone}")
print(f"email = {person1.email}")
print('-' * 80)

# create another referenced object of Person class
# person2 becomes self when the initializer gets called
person2 = Person()
print(f"person2 = {person2}")
print(f"name = {person2.name}")
print(f"address = {person2.address}")
print(f"age = {person2.age}")
print(f"phone = {person2.phone}")
print(f"email = {person2.email}")
print('-' * 80)

# update the data for person2
person2.name = "person2"
person2.address = "mumbai"
person2.age = 50
person2.email = "person2@test.com"
person2.phone = "+912356566"

print(f"person2 = {person2}")
print(f"name = {person2.name}")
print(f"address = {person2.address}")
print(f"age = {person2.age}")
print(f"phone = {person2.phone}")
print(f"email = {person2.email}")

# create another anonymous object of Person class
# anonymous object: object without any reference
Person()
print('-' * 80)

Person()
print('-' * 80)

