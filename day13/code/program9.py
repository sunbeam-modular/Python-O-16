# hybrid inhertiance

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.id = emp_id

class Player(Person):
    def __init__(self, name, team_name):
        super().__init__(name)
        self.team_name = team_name

class Manager(Employee):
    def __init__(self, name, emp_id, department_id):
        super().__init__(name, emp_id)
        self.department_id = department_id

person = Person("person1")
employee = Employee("employee1", 1)
player = Player("player1", "team1")
manager = Manager("manager1", 1, "HR")