class Person:
    # class members
    dummy_member = 10

print(f"dummy_member = {Person.dummy_member}")

# create an object of Person class
person1 = Person()
print(f"person1.dummy_member = {person1.dummy_member}")

# create another object of Person class
person2 = Person()
print(f"person2.dummy_member = {person2.dummy_member}")

# since person1 object is modifying the class member
# a new copy of dummy_member gets added to the person1
person1.dummy_member = 100
print(f"person1.dummy_member = {person1.dummy_member}")
print(f"person2.dummy_member = {person2.dummy_member}")
print(f"dummy_member         = {Person.dummy_member}")