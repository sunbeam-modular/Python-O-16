# closure function
def log(function):
    # print(f"inside log")

    # variable length arguments function
    def inner(*args, **kwargs):
        # open a log file for logging the data
        file = open('logs.txt', 'a')
        
        # log the data in a file
        file.write(f"function called: {function.__name__}\n")
        file.write(f"args  : {args}\n")
        file.write(f"kwargs: {kwargs}\n")
        
        # make a call to the function
        function(*args, **kwargs)

        file.write("-" * 80)
        file.write('\n')

        # close the file
        file.close()

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

@log
def square(n1: int):
    print(f"square of {n1} = {n1 ** 2}")

add(10, 20)
subtract(10, 20)
divide(10, 20)
multiply(10, 20)
square(10)