class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def display(self):
        print(f"name    = {self._name}")
        print(f"age     = {self._age}")

class Employee(Person):
    def __init__(self, id, company_name, name, age):
        super().__init__(name, age)
        self._id = id
        self._company_name = company_name

    # Employee is overriding the display() method
    def display(self):
        print(f"id      = {self._id}")
        print(f"company = {self._company_name}")

        # since the parent class (Person) has already implemented the following logic
        # there is no need to implement the logic again here
        # print(f"name    = {self._name}")
        # print(f"age     = {self._age}")

        # instead, call the super class method here
        super().display()

class Player(Person):
    def __init__(self, name, age, team):
        super().__init__(name, age)
        self._team = team

    # Player class is overriding the display() method
    def display(self):
        # since the parent class (Person) has already implemented the following logic
        # there is no need to implement the logic again here
        # print(f"name    = {self._name}")
        # print(f"age     = {self._age}")
        
        # instead, call the display method from Person class
        # super().display()
        Person.display(self)
        print(f"team    = {self._team}")


# create a Person object
person = Person("person1", 40)

# this statement will call display() from Person class
person.display()
print('-' * 80)

# create an Employee object
employee = Employee(1, 'company1', 'employee 1', 40)

# this statement will call display() from Employee class
employee.display()
print('-' * 80)

# create an object of Player class
player = Player("player1", 40, "team-india")
player.display()