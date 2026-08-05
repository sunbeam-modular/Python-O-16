class Employee:
    # initializer
    def __init__(self, employee_id, name, salary):
        # private members
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary

    # setter for name
    def set_name(self, name):
        self.__name = name

    # setter for salary
    def set_salary(self, salary):
        self.__salary = salary

    # getter for id
    def get_id(self):
        return self.__employee_id

    # getter for name
    def get_name(self):
        return self.__name

    # getter for salary
    def get_salary(self):
        return self.__salary

    # facilitator
    def display(self):
        print(f"id     = {self.__employee_id}")
        print(f"name   = {self.__name}")
        print(f"salary = {self.__salary}")
        print('-' * 80)

    # facilitator
    def increment_salary(self, by_percent):
        self.__salary += (self.__salary * (by_percent/100))

# create an object of Employee class
employee1 = Employee(1, "employee 1", 15000)
employee1.display()
employee1.increment_salary(10)
employee1.display()