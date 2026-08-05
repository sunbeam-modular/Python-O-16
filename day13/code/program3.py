# Composition
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
    def __init__(self, employee_id, name, salary, laptop_brand, laptop_ram, laptop_cpu):
        self.id = employee_id
        self.name = name
        self.salary = salary

        # create a new object of Laptop class
        self.laptop = Laptop(laptop_brand, laptop_ram, laptop_cpu)

    def display(self):
        print(f"id     = {self.id}")
        print(f"name   = {self.name}")
        print(f"salary = {self.salary}")

        # print laptop details
        print(f"laptop = {self.laptop.display()}")

class Person:
    def __init__(self, name, age, laptop_brand, laptop_ram, laptop_cpu):
        self.name = name
        self.age = age

        # create a new object of Laptop class
        self.laptop = Laptop(laptop_brand, laptop_ram, laptop_cpu)

    def display(self):
        print(f"name   = {self.name}")
        print(f"age    = {self.age}")
        print(f"laptop = {self.laptop.display()}")


# create an employee
employee = Employee(1, "Amit", 20000, "Apple MacBook", "16GB", "M2 Pro")
employee.display()

print("-" * 80)

# create a Person
person = Person("person1", 40, "Dell Inspirio", "16GB", "Intel Core i9")
person.display()


