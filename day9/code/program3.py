# multi-dimensional collection
# - collection of collections (nested collections)
# - e.g.
#   - list of lists
#   - list of tuples
#   - tuple of lists
#   - tuple of tuples
#   - list of dictionaries
#   - dictionary of lists or tuples or dictionaries

def function1():
    # create a 2d list (list of lists) of 3x2 size
    # - 3 rows and 2 columns
    numbers = [
        [10, 20],
        [30, 40],
        [50, 60]
    ]

    # get the values in outer list
    print(f"numbers[0]      = {numbers[0]}")
    print(f"numbers[1]      = {numbers[1]}")
    print(f"numbers[2]      = {numbers[2]}")
    print('-' * 80)

    # contents of first nested list
    print(f"numbers[0][0]   = {numbers[0][0]}")
    print(f"numbers[0][1]   = {numbers[0][1]}")
    print('-' * 80)

    # contents of second nested list
    print(f"numbers[1][0]   = {numbers[1][0]}")
    print(f"numbers[1][1]   = {numbers[1][1]}")
    print('-' * 80)

    # contents of third nested list
    print(f"numbers[2][0]   = {numbers[2][0]}")
    print(f"numbers[2][1]   = {numbers[2][1]}")
    print('-' * 80)

    # get all the values dynamically
    for row in numbers:
        print(f"row = {row}")
        for col in row:
            print(f"col = {col}")
    print('-' * 80)

    # since the numbers is list of lists
    # both the outer list as well as inner list can be modified
    print(f"numbers = {numbers}")

    # append a new row
    numbers.append([70, 80])
    print(f"numbers = {numbers}")

    # add a new column in a row
    numbers[3].append(90)
    print(f"numbers = {numbers}")

# function1()

def function2():
    # list of tuples
    numbers = [
        (10, 20),
        (30, 40),
        (50, 60)
    ]

    # get the values in outer list
    print(f"numbers[0]      = {numbers[0]}")
    print(f"numbers[1]      = {numbers[1]}")
    print(f"numbers[2]      = {numbers[2]}")
    print('-' * 80)

    # contents of first nested list
    print(f"numbers[0][0]   = {numbers[0][0]}")
    print(f"numbers[0][1]   = {numbers[0][1]}")
    print('-' * 80)

    # contents of second nested list
    print(f"numbers[1][0]   = {numbers[1][0]}")
    print(f"numbers[1][1]   = {numbers[1][1]}")
    print('-' * 80)

    # contents of third nested list
    print(f"numbers[2][0]   = {numbers[2][0]}")
    print(f"numbers[2][1]   = {numbers[2][1]}")
    print('-' * 80)

    # get all the values dynamically
    for row in numbers:
        print(f"row = {row}")
        for col in row:
            print(f"col = {col}")
    print('-' * 80)

    # since numbers is a list of tuples
    # the outer collection is mutable while inner collection is immutable
    print(f"numbers = {numbers}")

    # add a new row
    numbers.append((70, 80))
    print(f"numbers = {numbers}")

    # add a new column in a row is not possible anymore since the rows are tuples (which are immutable collection)
    # numbers[3].append(90)

# function2()

def function3():
    # tuple of lists
    numbers = (
        [10, 20],
        [30, 40],
        [50, 60]
    )
    print(f"numbers = {numbers}")

    # accessing the elements from tuple of list is same as accessing elements from list of lists
    # - please refer function1 or function2

    # since numbers is tuple of lists
    # adding row is not possible as the outer collection is immutable
    # numbers.append([70, 80])

    # adding a column in existing row is possible
    numbers[2].append(70)
    print(f"numbers = {numbers}")

# function3()

def function4():
    # tuple of tuples
    numbers = (
        (10, 20),
        (30, 40),
        (50, 60)
    )
    print(f"numbers = {numbers}")

    # accessing the elements from tuple of tuples is same as accessing elements from list of lists
    # - please refer function1 or function2

    # since numbers is tuple of tuples
    # adding row is not possible as the outer collection is immutable
    # numbers.append([70, 80])

    # adding a column in existing row is NOT possible as rows are now immutable
    # numbers[2].append(70)

# function4()

def function5():
    # list of person dictionaries
    persons = [
        {'name': 'john', 'age': 30, 'address': 'pune'},
        {'name': 'alice', 'age': 40, 'address': 'karad'},
        {'name': 'bob', 'age': 50, 'address': 'usa'}
    ]

    # iterate over all persons
    for person in persons:
        print(f"person  = {person}, type = {type(person)}")
        print(f"name    = {person['name']}")
        print(f"age     = {person['age']}")
        print(f"address = {person['address']}")

        # print all key-value pairs
        # for key, value in person.items():
        #     print(f"{key} = {value}")

# function5()

def function6():
    # dictionary with lists or tuples or dictionaries
    car = {
        "model": "triber",
        "company": "renault",

        # value as dictionary
        "attributes": {
            "mileage": 16,
            "color": "silver"
        },

        # value as list or tuple
        "accessories": ['footguard', 'seat covers']
    }

    # access all the values
    print(f"model   = {car['model']}")
    print(f"company = {car['company']}")

    # access all the attributes (of type dictionary)
    print(f"mileage = {car['attributes']['mileage']}")
    print(f"color   = {car['attributes']['color']}")

    # access all the accessories (of type list)
    for accessory in car['accessories']:
        print(f"accessory = {accessory}")

function6()

