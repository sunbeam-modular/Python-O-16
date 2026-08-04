# define a person class to store person details
# - name, address, age, phone, email

class Person:
    def __init__(self, name, address, age, phone, email):

        # add new members to the current object
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone
        self.email = email

# person1 becomes self

# at the time of compilation, compiler modifies the following statement
# person1 = Person("person1", "pune", 40, "+91123456", "person1@test.com") 
# => Person.__init__(person1, "person1", "pune", 40, "+91123456", "person1@test.com")
person1 = Person("person1", "pune", 40, "+91123456", "person1@test.com")
print(f"name = {person1.name}")
print(f"address = {person1.address}")
print(f"age = {person1.age}")
print(f"phone = {person1.phone}")
print(f"email = {person1.email}")

print('-' * 80)

# person2 becomes self
# at the time of compilation, compiler modifies the following statement
# person2 = Person(....) => Person.__init__(person2, ...)
person2 = Person("person2", "mumbai", 50, "+912344546", "person2@test.com")
print(f"name = {person2.name}")
print(f"address = {person2.address}")
print(f"age = {person2.age}")
print(f"phone = {person2.phone}")
print(f"email = {person2.email}")
