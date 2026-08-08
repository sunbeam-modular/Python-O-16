def add(p1: int, p2: int):    
    print(f"{p1} + {p2} = {p1 + p2}")

def subtract(p1: int, p2: int):
    print(f"{p1} - {p2} = {p1 - p2}")

def divide(p1: int, p2: int):
    print(f"{p1} / {p2} = {p1 / p2}")

def multiply(p1: int, p2: int):
    print(f"{p1} * {p2} = {p1 * p2}")

# add(10, 20)
# subtract(10, 20)
# divide(10, 20)
# multiply(10, 20)


# the log function is modifying the function beahvior 
# without modifying the function code
def log(function, p1, p2):
    # log the data
    print(f"p1 = {p1}, p2 = {p2}")

    # make a call to the function
    function(p1, p2)

# excute is now going to accept the add function reference
# log(add, 10, 20)
# log(subtract, 10, 20)
# log(divide, 10, 20)
# log(multiply, 10, 20)
