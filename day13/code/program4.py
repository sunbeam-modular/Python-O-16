# single inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name = {self.name}")
        print(f"age  = {self.age}")

# Employee is derived from Person class
# Employee is a child class of Person class
# Employee is subclass of Person class
class Employee(Person):
    pass

# print(f"Employee's base class = {Employee.__base__}")

# create a person class object
person = Person("person1", 30)
person.display()
print('-' * 80)

# create employee class object
employee = Employee("employee1", 40)
employee.display()