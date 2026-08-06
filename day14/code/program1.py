class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def display(self):
        print("called from Person class")
        print(f"name = {self._name}")
        print(f"age  = {self._age}")

        # Person class can NOT access any member of Employee class
        # print(f"id   = {self._id}")

class Employee(Person):
    def __init__(self, id, company_name, name, age):

        # initialize an object of parent class
        super().__init__(name, age)
        self._id = id
        self._company_name = company_name


# create a Person object
person = Person("person1", 40)
person.display()
print('-' * 80)

# create an Employee object
employee = Employee(1, 'company1', 'employee 1', 40)

# since Employee does not implement the display(), 
# this statement will the display() from Person class
# because of this, employee id and company name are missing in the output
employee.display()