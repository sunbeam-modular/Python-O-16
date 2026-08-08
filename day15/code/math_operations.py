# class definition
class Math:
    def __init__(self):
        pass

# list of functions
def add(p1: int, p2: int):    
    print(f"{p1} + {p2} = {p1 + p2}")

def subtract(p1: int, p2: int):
    print(f"{p1} - {p2} = {p1 - p2}")

def divide(p1: int, p2: int):
    print(f"{p1} / {p2} = {p1 / p2}")

def multiply(p1: int, p2: int):
    print(f"{p1} * {p2} = {p1 * p2}")

# constant
PI = 3.14

print(f"module name = {__name__}")

# this statement is NOT the entry point function of python
def main():
    # call the functions for testing
    add(10, 20)
    subtract(10, 20)
    multiply(10, 20)
    divide(10, 20)
    print(f"PI = {PI}")

# check if this module is being executed directly
if __name__ == '__main__':
    main()