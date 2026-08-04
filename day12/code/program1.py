# procedure oriented programming
# - programming with function (procedures)
# - simple and easy to debug
# - the data and operations can not be bound together

# operations which can be performed on the person data
def can_vote(person: dict):
    if person['age'] >= 18:
        print(f"{person['name']} is eligible")
    else:
        print(f"{person['name']} is NOT eligible")

def print_person_details(person: dict):
    print(f"name    = {person['name']}")
    print(f"address = {person['address']}")
    print(f"age     = {person['age']}")

# person information (data)
person = {
    "name": "person1",
    "address": "pune",
    "age": 40
}

# work for person dictionary
# can_vote(person)
# print_person_details(person)

# this line will raise an error
# can_vote(100)