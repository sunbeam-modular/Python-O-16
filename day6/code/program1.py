# list
# - collection of similar or dissimilar values
# - list is a mutable collection: the collection can be modified after it gets created
# - ordered collection: the values will read in the same order of insertion
# - allows duplicate values
# - built-in functions
#   - len(): get the length of collection
#   - min(): get the minimum value of the list of numbers
#   - max(): get the maximum value of the list of numbers
#   - sum(): get the addition of all the number values of a list
#   - any()
#     - check if there is any value present inside the collection
#     - in other words, check if the collection is empty or not
#   - sorted()
#     - used to get the collection in sorted (ascending) order. 
#     - does not update or modify the original collection
#     - rather it returns a new collection with sorted values
#  - reversed()
#    - used to get the collection in reverse order
#    - does not update or modify the original collection
#     - rather it returns a new collection with reversed values


def function1():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}, type = {type(numbers)}")

    # list of strings
    person_names = ["steve", "john", "alice", "bob"]
    print(f"person_names = {person_names}, type = {type(person_names)}")

    # list of mixed values
    mixed_values = [10, 50.40, "person1", True, 10 + 7j]
    print(f"mixed_values = {mixed_values}, type = {type(mixed_values)}")

# function1()

def function2():
    # list of numbers
    numbers = [20, 10, 60, 45, 78, 90, 25, 38, 94]
    print(f"numbers = {numbers}, type = {type(numbers)}")
    print()

    print(f"length of numbers                     = {len(numbers)}")
    print(f"minimum value of the numbers          = {min(numbers)}")
    print(f"maximum value of the numbers          = {max(numbers)}")
    print(f"sum of all values                     = {sum(numbers)}")

    # check if the collection contains any of the values or not
    print(f"any of the list values                = {any(numbers)}")
    print(f"sorted collection in ascending order  = {sorted(numbers)}")
    print(f"sorted collection in descending order = {sorted(numbers, reverse=True)}")
    print(f"reversed collection                   = {list(reversed(numbers))}")

# function2()

def function3():
    # list of string values
    person_names = ["alice", "bob", "steve", "arnold", "will", "jason"]
    print(f"person_names                          = {person_names}")
    print(f"sorted in ascending order of values   = {sorted(person_names)}")
    print(f"sorted in descending order of values  = {sorted(person_names, reverse=True)}")

    # here len is the reference of built in function
    print(f"sorted in ascending order of length   = {sorted(person_names, key=len)}")
    print(f"sorted in descending order of length  = {sorted(person_names, key=len, reverse=True)}")

    print(f"reversed collection                   = {list(reversed(person_names))}")
    
# function3() 

def function4():
    # repeatition operation
    print(f"[5] * 10        = {[5] * 10}")
    print(f"['sunbeam'] * 5 = {['sunbeam'] * 5}")
    print(f"[10, 5, 6] * 3  = {[10, 5, 6] * 3}")

    # string: collection of characters
    print(f"'-' * 50        = {'-' * 50}")
    print(f"'-|-' * 10      = {'-|-' * 10}")
    print(f"'*-*|' * 10     = {'*-*|' * 10}")

    # execute function3 5 times
    # note: this statement will not work as * does not support the operand types function and int
    # function3 * 5

function4()