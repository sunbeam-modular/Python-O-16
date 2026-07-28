# indexing
# - accessing items from collection
# - positive indexing
#   - the index positions start from zero to size of list - 1
#   - the positive index always starts from 0
# - negative indexing
#   - the index positions are negative values 
#   - the last value has a position of -1
#   - the second last value has a position of -2
#   - the first value has a position (-len(collection))
#   - though a python developer can use negative indexing, 
#     python converts the negative index to positive before accessing the element
#   - e.g. -3 negative is = len(collection) - 3 => positive index
#   - e.g. in a list of 5 values, -3 = 5 - 3 = 2

def function1():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers    = {numbers}")

    # access the items from collection using +ve indexing
    print(f"numbers[0] = {numbers[0]}")
    print(f"numbers[1] = {numbers[1]}")
    print(f"numbers[2] = {numbers[2]}")
    print(f"numbers[3] = {numbers[3]}")
    print(f"numbers[4] = {numbers[4]}")

    # since 5th index does not exist in numbers, this statement will raise IndexError
    print(f"numbers[5] = {numbers[5]}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers     = {numbers}")

    # access the items using negative index positions
    print(f"numbers[-1] = {numbers[-1]}")
    print(f"numbers[-2] = {numbers[-2]}")
    print(f"numbers[-3] = {numbers[-3]}")
    print(f"numbers[-4] = {numbers[-4]}")
    print(f"numbers[-5] = {numbers[-5]}")

function2()