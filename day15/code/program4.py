def function1():
    print("inside function1")

    # when next() is called, value 1 is returned and execution stops at the next statement
    yield 1

    # when next() is called, the execution resumes from the next statement
    print(f"after yield 1")
    yield 2

    # when next() is called, the execution resumes from the next statement
    print(f"after yield 2")
    yield 3

    # when next() is called, the execution resumes from the next statement
    print(f"after yield 3")
    yield 4

# generator_object = function1()
# print(f"generator_object = {generator_object}, type = {type(generator_object)}")

# print(f"next value = {next(generator_object)}")
# print(f"next value = {next(generator_object)}")
# print(f"next value = {next(generator_object)}")
# print(f"next value = {next(generator_object)}")

def function2(n):
    numbers = []
    for index in range(n):
        numbers.append(index)
    return numbers

# numbers will be having 10000 values
# the memory for all the values will be allocated immediately after calling the function
# numbers = function2(10000)
# print(f"numbers = {numbers}")

def function3(n):
    for index in range(n):
        yield index

numbers = function3(10000)
print(f"numbers = {numbers}")

# lazy evaluation
# - since the next() is called 5 times, only 5 memory blocks will be allocated
print(f"value   = {next(numbers)}")
print(f"value   = {next(numbers)}")
print(f"value   = {next(numbers)}")
print(f"value   = {next(numbers)}")
print(f"value   = {next(numbers)}")
