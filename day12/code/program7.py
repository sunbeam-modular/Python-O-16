class Person:
    def __init__(self, name, age, salary):
        # public member
        self.name = name

        # private member
        self.__age = age
        self.__salary = salary

    # facilitator
    def print_details(self):
        print(f"name = {self.name}")
        print(f"age  = {self.__age}")
        print(f"salary  = {self.__salary}")
        print('-' * 80)

    # facilitator
    def can_vote(self):
        if self.__age >= 18:
            print(f"{self.name} is eligible for voting")
        else:
            print(f"{self.name} is NOT eligible for voting")

    # setter to set/update age 
    def set_age(self, age):
        # since the __age is private member, it is accessible inside the class

        # validation
        # - making sure the data is valid before it gets set to the member
        # - range of valid value depends upon the problem
        if age >= 18 and age < 80:
            self.__age = age

    # getter to get age value
    def get_age(self):
        # return the current value of __age property
        return self.__age

    # getter to get salary value
    def get_salary(self):
        return self.__salary

# create an object of Person class
person1 = Person('person', 40, 50000)
person1.can_vote()
person1.print_details()

# update the person details
# accessing the members is allowed outside the class
person1.name = "person2"

# age can get invalid value
# person1.age = -50

# since the __age is a private member, setting value to it, wont change anything
# person1.__age = -50

# even if the value 41 is valid, __age (private member) wont accept it
# person1.__age = 41

person1.set_age(5)
person1.print_details()

# since the __age is a private member, it can NOT be accessed outside the class
# the following statement will raise an error
# print(f"age = {person1.__age}")
print(f"age = {person1.get_age()}")

# calculate bonus at 10%
bonus = person1.get_salary() * 0.10
print(f"bonus = {bonus}")
