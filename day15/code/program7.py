# closure function
def log(function):
    # print(f"inside log")

    def inner(p1, p2):
        # log the data
        print(f"p1 = {p1}, p2 = {p2}")
    
        # make a call to the function
        function(p1, p2)
        print()

    # return inner function reference
    return inner

@log
def add(p1: int, p2: int):    
    print(f"{p1} + {p2} = {p1 + p2}")

@log
def subtract(p1: int, p2: int):
    print(f"{p1} - {p2} = {p1 - p2}")

@log
def divide(p1: int, p2: int):
    print(f"{p1} / {p2} = {p1 / p2}")

@log
def multiply(p1: int, p2: int):
    print(f"{p1} * {p2} = {p1 * p2}")

add(10, 20)
subtract(10, 20)
divide(10, 20)
multiply(10, 20)