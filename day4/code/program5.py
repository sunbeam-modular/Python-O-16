def function1(p1, p2):
    """"""
    print(f"inside function1")
    print(f"p1 = {p1}, p2 = {p2}")

# function1(10, 20)

# function declaration with type hinting
# since this function is not returning anything explicitly (using return keyword),
# the default value it returns implicitly is None
def function2(p1: int, p2: int) -> None:
    """"""
    print(f"inside function2")
    print(f"p1 = {p1}, p2 = {p2}")
    print(f"{p1} + {p2} = {p1 + p2}")

# function2(10, 20)
# function2(10, 20.50)

# result = function2(10, 20)
# print(f"result = {result}, type = {type(result)}")

# type hinting is not for the compiler
# this line will work
# - in python, all data types are inferred
# function2("test1", "test2")

# there is not compile time error but the code will crash 
# function2(10, "test")


# function optionally can return a value to the caller
# the caller may capture the returned value in a variable
def add(p1: int, p2: int):
    # add p1 and p2
    result = p1 + p2

    # return the result to the caller
    return result


# call the function add with 20 and 30 arguments 
# and capture the addition result in a variable named addition
# addition = add(p1=20, p2=30)
# print(f"addition = {addition}")

# this function is accepting two integers 
# and returning an integer value
# here '-> int' means: subtract function returns an integer result
def subtract(p1: int, p2: int) -> int:
    # get the subtration result
    result = p1 - p2

    # return result to the caller
    return result

# call subtract and capture returned value int subtraction variable
# subtraction = subtract(30, 10)
# print(f"subtraction = {subtraction}")

# before returning the value, the expression will be solved
def multiply(p1: int, p2: int) -> int:
    return p1 * p2

# multiplication = multiply(3, 7)
# print(f"multiplication = {multiplication}")