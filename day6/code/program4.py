# list methods
# count(value)
# - used to get the number of times the valus is present in the collection
# - if the value does not exist, count() returns 0
# index(value)
# - by default, used to get the position of first occurance of the value
# - is the value does not exist, the index() raises an error
# index(value, start_index)
# - starts finding the value in the collection from start_index
# - when the required value is found, it stops
# - the default value of start_index is 0, which is why only the first occurance posiion will be returnd
# - but if the start_index is passed, the index() will return the position of other occurances as well


def function1():
    # list of numbers
    numbers = [18, 20, 40, 30, 70, 10, 40, 60, 20, 50, 70, 20, 70]
    print(f"numbers   = {numbers}")

    # check how many times value 70 is present
    print(f"value 70 is present = {numbers.count(70)} times")

    # check how many times value 20 is present
    print(f"value 20 is present = {numbers.count(20)} times")

    # check how many times value 100 is present
    print(f"value 100 is present = {numbers.count(100)} times")

# function1()

def function2():
    # list of numbers
    numbers = [18, 20, 40, 30, 70, 10, 40, 60, 20, 50, 70, 20, 70]
    print(f"numbers   = {numbers}")

    # find the position of first occurance of value 20
    print(f"value 20 is present at {numbers.index(20)} position")

    # find the position of value 20
    # start searching for the value from 2nd position instead of 0th one
    print(f"value 20 is present at {numbers.index(20, 2)} position")

    # find the position of first occurance of value 20
    print(f"value 20 is present at {numbers.index(20, 9)} position")

    # find the position of value 100
    # print(f"value 100 is present at {numbers.index(100)} position")

function2()
