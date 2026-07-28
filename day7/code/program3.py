# range()
# - used to create a collection of sequential values
# - parameters
#   - start
#     - start position where the collection begins
#     - has a default value 0
#     - can be passed optionally
#   - stop
#     - stop positin where the sequence generation stops
#     - stop position is NOT included in the sequence
#   - step
#     - used to generate the next value
#     - default value of step is 1
#     - since it has default value, it an optional parameter


def function1():
    # generate a sequence from 0 to 10 with step count 1
    numbers = list(range(0, 10, 1))
    print(f"range(0, 10, 1)     = {numbers}")

    # generate a sequence from 0 to 10 with step count 1
    numbers = list(range(0, 10))
    print(f"range(0, 10)        = {numbers}")

    # generate a sequence from 0 to 10 with step count 1
    numbers = list(range(10))
    print(f"range(10)           = {numbers}")

# function1()

def function2():
    # print hello world 5 times
    for index in range(5):
        print(f"hello world {index}")

# function2()

def function3():
    # generate sequence from 0 to 10 by adding 1 to existing value
    print(f"range(0, 10, 1)   = {list(range(0, 10, 1))}")

    # generate sequence from 0 to 10 by adding 2 to existing value
    print(f"range(0, 10, 2)   = {list(range(0, 10, 2))}")

    # generate sequence from 0 to 10 by adding 3 to existing value
    print(f"range(0, 10, 3)   = {list(range(0, 10, 3))}")

# function3()

def function4():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # iterate over all the values
    # for value in numbers:
    #     print(f"value = {value}")

    # iterate from 3rd position till 7th positition
    # similar to traditional for loop in C
    # -> for (int index = 3; index < 8; index++) {...}
    for index in range(3, 8):
        print(f"value at {index} = {numbers[index]}")

function4()

