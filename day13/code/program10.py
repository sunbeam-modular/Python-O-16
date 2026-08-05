# Single inheritance

# parent class
class Person:
    def __init__(self, name, age):
        # public member
        self.public_property = "test"

        # protected members
        self._name = name
        self._age = age

        # private member
        self.__property = "private property"

    def display(self):
        print(f"name     = {self._name}")
        print(f"age      = {self._age}")
        print(f"property = {self.__property}")

# child class
class Employee(Person):
    def __init__(self, emp_id, name, age, salary):
        super().__init__(name, age)

        # protected members
        self._id = emp_id
        self._salary = salary

    def display(self):
        print(f"id     = {self._id}")
        print(f"name   = {self._name}")
        print(f"age    = {self._age}")
        print(f"salary = {self._salary}")

        # child class can NOT access the private member(s) of parent classes
        # print(f"property = {self.__property}")

# create a person class object
person = Person("person1", 30)
person.display()

print(f"outside Person, public_property = {person.public_property}")
# print(f"outside Person, name = {person._name}")
print('-' * 80)

# create employee class object
employee = Employee(1, "employee1", 40, 15000)
employee.display()

# print(f"outside Employee, name = {employee._name}")
