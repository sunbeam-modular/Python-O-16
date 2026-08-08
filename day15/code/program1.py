def function1():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}")
    print('-' * 80)

    # iterate over the list
    for number in numbers:
        print(f"number  = {number}")
    print('-' * 80)

    # string
    article = "this is a sample article"
    for ch in article:
        print(f"ch = {ch}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}")
    print('-' * 80)

    # get the iterator object
    numbers_iterator = iter(numbers)
    print(f"numbers_iterator = {numbers_iterator}")

    # get the next value
    print(f"next value = {next(numbers_iterator)}")
    print(f"next value = {next(numbers_iterator)}")
    print(f"next value = {next(numbers_iterator)}")
    print(f"next value = {next(numbers_iterator)}")
    print(f"next value = {next(numbers_iterator)}")

    # this statement will raise an exception named StopIteration
    # print(f"next value = {next(numbers_iterator)}")

# function2()
