# list methods to add value
# - these methods will work on a list, irrespective of the type of values inside the list
# - most of the methods update the original collection
#   - append, insert, clear, pop, reverse, sort, remove
# append(): used to add a single new value at the end of the collection
# insert(): used to insert a value in between the collection
# extend(): used to add multiple values at the end of the collection (individually)

def function1():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers      = {numbers}")

    # append a value at the end of the collection
    numbers.append(60)
    print(f"numbers      = {numbers}")

    # append a value at the end of the collection
    numbers.append(70)
    print(f"numbers      = {numbers}")

# function1() 

def function2():
    # empty of peson names
    person_names = []
    print(f"person_names    = {person_names}")

    # infinite loop: the loop which never stops/breaks automatically
    while True:

        # collect person names from user
        name = input("enter person name: ")
        person_names.append(name)

        # ask whether use wants to stop
        result = input("are you done with entering names (y/n): ")

        # if user wants to stop, break the loop
        if result == 'y' or result == 'Y':

            # explicitly stop the loop
            break

    print(f"person_names    = {person_names}")

# function2()

def function3():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers        = {numbers}")

    # insert()
    # - param1: position where the value needs to add
    # - param2: value to be added on the position

    # insert value 15 betwen 10 and 20
    # insert the value 15 on 1st position
    # when the value 15 gets inserted on the 1st position, all the remaining values will be shifted to the right side
    numbers.insert(1, 15)
    print(f"numbers        = {numbers}")

    # insert value 25 between 20 and 30
    numbers.insert(3, 25)
    print(f"numbers        = {numbers}")

    # insert value 35 between 30 and 40
    numbers.insert(5, 35)
    print(f"numbers        = {numbers}")

    # insert value 45 between 40 and 50
    numbers.insert(7, 45)
    print(f"numbers        = {numbers}")

# function3()

def function4():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers           = {numbers}")
    print(f"length of numbers = {len(numbers)}")

    # append value 60, 70, 80, 90 and 100 at the end of the list
    numbers.extend([60, 70, 80, 90, 100])
    print(f"numbers           = {numbers}")
    print(f"length of numbers = {len(numbers)}")

function4()