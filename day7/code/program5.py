# tuple
# - immutable ordered collection of similar or dissimilar values
# - once created, it can NOT be changed
# - () may or may not be used while creating a tuple object
# - tuple packing:
#   - () are not used while creating a tuple
#   - e.g. tuple1 = 10, 20, 30, 40, 50
# - since it is an immutable collection, it does NOT support following methods
#   - append()
#   - extends()
#   - insert()
#   - remove()
#   - pop()
#   - clear()
#   - sort()
#   - reverse()
#   - copy()
# - tuple only supports following methods
#   - count(): get occurance of a value
#   - index(): get the index of a value

def function1():
    # create an empty list
    list1 = []
    print(f"list1  = {list1}, type = {type(list1)}")

    # create an empty list
    list2 = list()
    print(f"list2  = {list2}, type = {type(list2)}")

    print('-' * 80)

    # create an empty tuple
    tuple1 = ()
    print(f"tuple1 = {tuple1}, type = {type(tuple1)}")

    # create an empty tuple
    tuple2 = tuple()
    print(f"tuple2 = {tuple2}, type = {type(tuple2)}")

# function1()

def function2():
    # list of numbers
    numbers_list = [10, 20, 30, 40, 50]
    print(f"numbers_list     = {numbers_list}, type = {type(numbers_list)}")

    # tuple of numbers
    numbers_tuple1 = (10, 20, 30, 40, 50)
    print(f"numbers_tuple1   = {numbers_tuple1}, type = {type(numbers_tuple1)}")

    # tuple of numbers
    # - pack the values 10, 20, 30, 40 and 50 in a tuple
    numbers_tuple2 = 10, 20, 30, 40, 50
    print(f"numbers_tuple2   = {numbers_tuple2}, type = {type(numbers_tuple2)}")

# function2()

def function3():
    # list of numbers
    numbers_list = [10, 20, 30, 40, 50]
    print(f"numbers_list     = {numbers_list}, type = {type(numbers_list)}")

    # convert the list object to a tuple
    numbers_tuple = tuple(numbers_list)
    print(f"numbers_tuple    = {numbers_tuple}, type = {type(numbers_tuple)}")

    # convert a tuple to a list
    numbers_list_new = list(numbers_tuple)
    print(f"numbers_list_new = {numbers_list_new}, type = {type(numbers_list_new)}")

# function3() 

def function4():
    # tuple of values
    numbers = (10, 20, 30, 40, 50)
    print(f"numbers     = {numbers}")

    # tuple does not support append()
    # numbers.append(60)

    # tuple does not support insert()
    # numbers.insert(1, 15)

    # get the count of value 40
    print(f"value 40 is repeated {numbers.count(40)} times")    

    # get the count of value 100
    print(f"value 100 is repeated {numbers.count(100)} times")    

    # get the index of value 40
    print(f"value 40 is present at {numbers.index(40)} position")

function4()
