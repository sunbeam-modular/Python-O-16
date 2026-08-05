# Aggregation
# - Employee has-a Laptop
# - Person has-a Laptop

class Laptop:
    def __init__(self, brand, ram, cpu):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu

    def display(self):
        return f"Laptop [brand: {self.brand:}, ram: {self.ram:}, cpu: {self.cpu:}]"

class Employee:
    def __init__(self, employee_id, name, salary, laptop):
        self.id = employee_id
        self.name = name
        self.salary = salary

        # employee has-a laptop
        self.laptop = laptop

    def display(self):
        print(f"id     = {self.id}")
        print(f"name   = {self.name}")
        print(f"salary = {self.salary}")

        # print laptop details
        print(f"laptop = {self.laptop.display()}")

class Person:
    def __init__(self, name, age, laptop):
        self.name = name
        self.age = age
        self.laptop = laptop

    def display(self):
        print(f"name   = {self.name}")
        print(f"age    = {self.age}")
        print(f"laptop = {self.laptop.display()}")


# create a laptop
laptop1 = Laptop("Apple MacBook", "16GB", "M2 Pro")

# create an employee
employee = Employee(1, "Amit", 20000, laptop1)
employee.display()

print("-" * 80)

# create another latop
laptop2 = Laptop("Dell Inspirio", "16GB", "Intel Core i9")

# create a Person
person = Person("person1", 40, laptop2)
person.display()


