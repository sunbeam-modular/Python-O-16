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
#   - '*' can not be the last symbol in the parameters list
# - positional only parameters
#   - the arguments for these parameters must be passed only with positional way
#   - a symbol '/' is used to make position-only parameters
#   - before the symbol '/', all the parameters must be passed as positional only
#   - '/' can not be the first symbol in the parameters list
# - combination of '/' and '*'
#   - '/' can not come after '*' in the parameters list
#   - keyword only parameters must be defined after positional only paramter

# only p1 must be passed as positional only
# p2 and p3 can be passed as positional or keyword
def function1(p1, /, p2, p3):
    """"""
    pass

# these lines will work
# function1(10, 20, 30)
# function1(10, 20, p3=30)
# function1(10, p2=20, p3=30)

# since p1 is passed as keyword arguent, this line wont work
# function1(p1=10, p2=20, p3=30)

# p1 and p2 must be passed as positional only
# p3 can be passed as positional or keyword
def function2(p1, p2, /, p3):
    """"""
    pass

# these lines will work
# function1(10, 20, 30)
# function1(10, 20, p3=30)

# these lines will NOT work
# function1(10, p2=20, p3=30)
# function1(p1=10, p2=20, p3=30)

# since there is no parameter before /, 
# this line will generate a compile time error
# def function2(/, p1, p2, p3):
#     """"""
#     pass

# all the parameters must be passed as positional only
def function2(p1, p2, p3, /):
    """"""
    pass


# p1 must be passed as positional only
# p4 and p5 must be passed as keyword only
# p2 and p3 can be passed as positional or keyword
def function3(p1, /, p2, p3, *, p4, p5):
    """"""
    pass

# this line will generate compile time syntax error
# because / can not come after * in the parameters list
# def function4(p1, *, p2, p3, /, p4, p5):
#     """"""
#     pass