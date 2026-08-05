# Single inheritance

# parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name = {self.name}")
        print(f"age  = {self.age}")

# child class
class Employee(Person):
    def __init__(self, emp_id, name, age, salary):
        # initialize the parent (Person) class object
        # super().__init__(name, age)

        # initialize the parent (Person) class object
        Person.__init__(self, name, age)

        # initialize the own members
        self.id = emp_id
        self.salary = salary

# create a person class object
person = Person("person1", 30)
person.display()
print('-' * 80)

# create employee class object
employee = Employee(1, "employee1", 40, 15000)
employee.display()