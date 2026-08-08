# variable length argument function
# - since kwargs is missing, function1 can accept only positional arguments
def function1(*args):
    print(f"inside function1")
    print(f"args  = {args}, type = {type(args)}")

# positional arguments: passing arguments using postion
# function1(10, 20)
# function1(10, 20, 30)
# function1(10, 20, 30, 40)

# keyword arguments: passing arguments along with their parameter name
# function1(p1=10, p2=20, p3=30)


# variable length argument function
# - function2 can accept positional as well as keyword arguments
def function2(*args, **kwargs):
    print(f"inside function1")
    print(f"args   = {args}, type = {type(args)}")
    print(f"kwargs = {kwargs}, type = {type(kwargs)}")

# positional arguments
# function2(10, 20)
# function2(10, 20, 30)

# keyword arguments
# function2(p1=20, p2=20, p3=30)

# positional and keyword arguments
# function2(10, 20, p1=30, p2=40)
