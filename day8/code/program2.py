# variable length arguments function
# - function which may receive variabe number of arguments
# - such function must be declared with a parameter having *
# - a parameter with * will accept variable length of arguments
# - args is a convention and not a compusion

def simple_add(p1, p2, p3=0, p4=0):
    result = p1 + p2 + p3 + p4
    print(f"result = {result}")

# simple_add(10, 20)
# simple_add(10, 20, 30)
# simple_add(10, 20, 30, 40)

# * here is not a pointer
# * here is used to receive all the arguments in a single variable
# this function is knows as variable length argument function
# this function can receive any number of arguments
# the parameter name is args (which can be any name but args is a convention)
# the parameter type is a tuple
def add(*args):
    # get the sum of all the values
    result = sum(args)
    print(f"args = {args}, type = {type(args)}, result = {result}")
    
# add(10, 20)
# add(10, 20, 30)
# add(10, 20, 30, 40)
# add(10, 20, 30, 40, 50)

# p1 must accept only one argument
# args may accept any number of arguments
# - in such functions, the variable length argument parameter must be at the end of the parameter's list
def function1(p1, *my_args):
    print(f"p1   = {p1}, type = {type(p1)}")
    print(f"args = {my_args}, type = {type(my_args)}")
    print('-' * 80)

function1(10)
function1(10, 20)
function1(10, 20, "test")
function1(10, 20, True, 40.50)