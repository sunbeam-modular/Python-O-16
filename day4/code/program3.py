# ways to pass arguments 
# - positional arguments
#   - the arguments will be passed with the same order of parameters declaration
#   - the order of arguments is very important
# - keyword arguments (named parameters)
#   - the arguments passed along with the parameter names
#   - the order of the arguments is not important as the argument is associated with its parameter name
# - combining positional and keyword arguments
#   - the positional arguments must be passed before the keyword arguments
# - default parameter
#   - the paramater having a default value
#   - since the default value is set at the time of function declaration, 
#     the parameter becomes optional
#   - it is also known as optional parameter
#   - all the default parameters must be on the right side of the function declaration
# - keyword only paramters
#   - the arguments for these parameters must be passed only with keyowrds and not as positional
#   - a symbol * is used to make it mandatory to pass the arguments using keywords
#   - after the '*' symbol, all the parameters must be passed as keyword arguments
#   - only one '*' is allowed in the function definition for making the parameters keyword only


# p1 can be passed as positional or keyword argument
# p2 and p3 must be passed as keyword arguments only
def function1(p1, *, p2, p3):
    """"""
    print("inside function1")
    print(f"p1 = {p1}, p2 = {p2}, p3={p3}")

# all arguments are passed as positional arguments
# this is not possible since p2 and p3 must be keyword arguments
# function1(10, 20, 30)

# two positional args and one keyword arg
# this is not possible since p2 and p3 must be keyword arguments
# function1(10, 20, p3=30)

# one positional arg and two keyword args
# function1(10, p2=20, p3=30)

# all keyword args
# function1(p1=10, p2=20, p3=30)


# p1 and p2 can be passed as positional or keyword
# it is mandatory to pass p3 as keyword argument only
def function2(p1, p2, *, p3):
    """"""
    print("inside function1")
    print(f"p1 = {p1}, p2 = {p2}, p3={p3}")

# this will not work
# function2(10, 20, 30)

# these lines will work
# function2(10, 20, p3=30)
# function2(10, p2=20, p3=30)
# function2(p1=10, p2=20, p3=30)


# all parameters must be passed as keyword only
def function3(*, p1, p2, p3):
    """"""
    print("inside function1")
    print(f"p1 = {p1}, p2 = {p2}, p3={p3}")


# all the function calls below will NOT work
# function3(10, 20, 30)
# function3(10, 20, p3=30)
# function3(10, p2=20, p3=30)

# this will work
# function3(p1=10, p2=20, p3=30)

def make_rectangle(x, y, width, height, *, color="black", is_filled=False, border_style="solid"):
    pass

make_rectangle(
    10, 20, 100, 200, 
    color="red", is_filled=True, border_style="solid"
)

make_rectangle(10, 20, 100, 200, is_filled=True, color="red")