# list methods to remove a value
# pop()
# - used to remove the last value the list
# - returns the value removed from the list
# pop(index_position)
# - used to remove a value from the list at indexth position
# - returns the value removed from the list
# - if the index does not exist in the list, the code raises an error IndexError
# remove(value)
# - by default used to remove a first occurance of a value from the collection 
#   using the actual value and not the position
# clear()
# - used to remove all values from the list collection

def function1():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers       = {numbers}")
    print('-' * 80)

    # remove the last value of the list
    removed_value = numbers.pop()
    print(f"numbers       = {numbers}")
    print(f"removed value = {removed_value}")
    print('-' * 80)

    # remove the last value of the list
    removed_value = numbers.pop()
    print(f"numbers       = {numbers}")
    print(f"removed value = {removed_value}")
    print('-' * 80)

    # remove the last value of the list
    removed_value = numbers.pop()
    print(f"numbers       = {numbers}")
    print(f"removed value = {removed_value}")
    print('-' * 80)

# function1()

def function2():
    # list of string values
    persons = ["steve", "john", "mathew", "alice", "json"]
    print(f"persons   = {persons}")

    # remove the last value 
    persons.pop()
    print(f"persons   = {persons}")

    # remove mathew from the list
    persons.pop(2)
    print(f"persons   = {persons}")

# function2()

def function3():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers   = {numbers}")

    # remove the value 30
    numbers.pop(2)
    print(f"numbers   = {numbers}")

    # remove the value 40
    numbers.pop(2)
    print(f"numbers   = {numbers}")

    # remove the value at 6th position
    # IndexError: pop index out of range
    # numbers.pop(6)
    # print(f"numbers   = {numbers}")

# function3()

def function4():
    # list of person names
    first_names = ["Emily", "Michael", "Jessica", "William", "Olivia", "James", 
        "Ava", "Robert", "Isabella", "Richard", "Sophia", "Charles", "Mia", 
        "Thomas", "Charlotte", "Donald", "Abigail", "Ronald", "Harper", "Kenneth"]

    # check is Sophia is present
    print(f"is Sophia present = {'Sophia' in first_names}")

    # remove Sophia from the collection
    # step1: find the index of Sophia

    # start the index position with 0
    index = 0
    for name in first_names:

        # check if the name is Sophia
        if name == 'Sophia':
            # found the requred name
            break

        # increment the index position
        index += 1

    # step 2: now the index of Sophia is known, call pop method to remove Sophia
    first_names.pop(index)

    # check is Sophia is present
    print(f"is Sophia present = {'Sophia' in first_names}")

# function4() 

def function5():
    # list of person names
    first_names = ["Emily", "Michael", "Jessica", "William", "Olivia", "James", 
        "Ava", "Robert", "Isabella", "Richard", "Sophia", "Charles", "Mia", 
        "Thomas", "Charlotte", "Donald", "Abigail", "Ronald", "Harper", "Kenneth"]

    # check is Sophia is present
    print(f"is Sophia present = {'Sophia' in first_names}")

    # remove Sophia from the list
    first_names.remove('Sophia')

    # check is Sophia is present
    print(f"is Sophia present = {'Sophia' in first_names}")

# function5()

def function6():
    # list of numbers
    numbers = [18, 20, 40, 30, 70, 10, 40, 60, 20, 50, 70, 20, 70]
    print(f"numbers   = {numbers}")

    # remove value 20 from numbers
    numbers.remove(20)
    print(f"numbers   = {numbers}")

# function6()

def function7():
    # list of numbers
    numbers = [18, 20, 40, 30, 70, 10, 40, 60, 20, 50, 70, 20, 70]
    print(f"numbers   = {numbers}")

    # remove the second occurance of the value 70
    # step1: find the index of first occurance
    index_first = numbers.index(70)
    print(f"value 70 is present on {index_first} index first time")

    # step2: find the index of second occurance
    index_second = numbers.index(70, index_first + 1)
    print(f"value 70 is present on {index_second} index second time")

    # step3: remove the value using the index of second occurance
    numbers.pop(index_second)
    print(f"numbers   = {numbers}")

# function7()

def function8():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}")

    # remove all values from numbers collection
    numbers.clear()
    print(f"numbers = {numbers}")

function8()
