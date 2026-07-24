# list
# - collection of similar or dissimilar values
# - is not similar to the array concept in C
# - the values will not be stored contigously
# - index starts at 0th position

def function1():
    # create an empty list
    empty_list1 = []
    print(f"empty_list1 = {empty_list1}, type = {type(empty_list1)}")

    # cerate an empty list
    empty_list2 = list()
    print(f"empty_list2 = {empty_list2}, type = {type(empty_list2)}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}, type = {type(numbers)}")

    # list of strings
    countries = ['india', 'usa', 'uk', 'japan']
    print(f"countries = {countries}, type = {type(countries)}")

    # list of booleans
    boolean_list = [True, False, False, True]
    print(f"boolean_list = {boolean_list}, type = {type(boolean_list)}")

    # list of mixed values
    mixed_values = [10, "india", True, False, 20, 40.50, 10 + 5j]
    print(f"mixed_values = {mixed_values}, type = {type(mixed_values)}")

# function2()

def function3():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]

    # get the length of a collection
    print(f"number of items in numbers = {len(numbers)}")

    # read the values from list
    print(f"value at 0th position = {numbers[0]}")
    print(f"value at 1st position = {numbers[1]}")

# function3()

def function4():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]

    # list of strings
    countries = ['india', 'usa', 'uk']

    # print all the items from a collection
    # loop statement
    # - there are two loop options in python
    # - while loop
    #   - used when the number of iteration is not known

    # for..in loop 
    # - used when the number of iterations is known
    # - automatically increments the index position
    # - implicitly starts at 0th position and goes till the end of the collection
    # - syntax:
    #   for <temp variable> in <collection>:
    #       # access value at each iteration using tmp variable
    for number in numbers:
        print(f"number = {number}")

    print()

    for country in countries:
        print(f"country = {country}")

# function4()

def function5():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]

    # get the enumerator
    # - enumerator is used to enumerate (iterate) over a collection
    for item in enumerate(numbers):
        print(f"item = {item}")

    print()

    # first variable will have an index position
    # second variable will have the actual value at the index position
    for position, value_at_position in enumerate(numbers):
        print(f"value at {position} = {value_at_position}")

# function5()


def function6():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]

    # while loop
    # - requires the index increment to be handled explicitly
    # - while loop continues iterations till the time the condition holds true
    # - while loop breaks when the condition returns false
    # - syntax
    #   while <condition>:
    #      # body of while loop
    # - till the time condition returns True, the while continues iterations

    # print all the values using while loop
    index = 0
    while index < len(numbers):

        # read the value at the index position
        print(f"value at {index} = {numbers[index]}")

        # increment the index position
        index += 1

function6()