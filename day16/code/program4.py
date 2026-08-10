# JSON
# - javascript object notation
# - syntax to make the data more readable
# - used to transfer data from one to another component (client to server)
# - contains types
#   - object
#     - similar to python dictionary
#     - collection of key-value pairs
#     - uses {}
#   - array
#     - similar to the list in python
#     - collection of values or objects
#     - uses []

import json

def function1():
    # create a dictionary
    person = {"name": "person1", "age": 20, "address": "pune"}
    print(f"person      = {person}, type = {type(person)}")

    # convert the dictionary to json object
    json_string = json.dumps(person)
    print(f"json_string = {json_string}, type = {type(json_string)}")

# function1()

def function2():
    # list of person data
    persons = [] 

    while True:
        # check if user has more to enter person data
        answer = input("Do you want to enter new person data (y/n): ")
        if answer == 'n':
            break

        # get input from user for creating person objects
        name = input("enter person name: ")
        age = int(input("enter age: "))
        address = input("enter address: ")
        email = input("enter email: ")

        # add the person data to the persons collection
        persons.append({
            "name": name, "age": age, "address": address, "email": email
        })

    # print all the data
    print(f"persons = {persons}")

    # open a new file to persist the contents
    file = open("persons.json", "w")

    # persist the data in JSON format
    file.write(json.dumps(persons, indent=4))

    # close the file
    file.close()

function2()

