# multi-level inheritance

# parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name = {self.name}")
        print(f"age  = {self.age}")

# child class of Person
class Employee(Person):
    def __init__(self, emp_id, name, age):
        super().__init__(name, age)
        self.id = emp_id

# child class of Employee
class Manager(Employee):
    def __init__(self, emp_id, name, age, department_id):
        super().__init__(emp_id, name, age)
        self.department_id = department_id

person = Person("person1", 30)
employee = Employee(1, "employee1", 40)
manager = Manager(10, "manager1", 50, "HR")