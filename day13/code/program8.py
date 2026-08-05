# hierarchical inhertiance

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.id = emp_id

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

class Player(Person):
    def __init__(self, name, team_name):
        super().__init__(name)
        self.team_name = team_name

person = Person("person1")
employee = Employee("employee1", 1)
student = Student("student1", 1)
player = Player("player1", "team1")