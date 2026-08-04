class Person:
    def __init__(self, name, age=40):
        print(f"__init__() called")
        self.name = name
        self.age = age
        # self.database_connection = ...
        # self.filename = open(....)

    def __del__(self):
        print(f"__del__() called for name = {self.name}")
        # if needed, store the data somewhere
        # close the connection
        # close the opened file

# create an object of Person class
person1 = Person(name="person1")
print(f"person1 = {person1}")

# create another object of Person class
person2 = Person(name="person2", age=50)
print(f"person2 = {person2}")

# create another object of Person class
person3 = Person(name="person3", age=20)
print(f"person3 = {person3}")
print('-' * 80)

print("statement 1")
print('-' * 80)

print(f"before deleteing person2, name = {person2.name}")

# person2 is not required anymore after this statement
# lets delete the object referenced by person2 explicitly
del person2

# note: since person2 is no longer avaiable, person2.name will raise an error
# print(f"after deleting person2,   name = {person2.name}")

print("statement 2")
print('-' * 80)

# since python supports garbage collection, 
# remaining all the objects will get deleted automatically at the end