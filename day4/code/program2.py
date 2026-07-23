# function definition
# - function declaration 
#   - function name
#   - list of function parameters
# - function body
#   - block of statements implementing the logic
# - in python, the function declaration and function body can NOT be separated
# - in python, a def keyword is used to define a function
# - pass: 
#   - passing the control to the next statement
#   - is the keyword used to create an empty function block

# function definition = function declaration + function body
# function declaration
def function1():
    # function docstring (document string)
    """contains the function description"""
    pass

# function call or invocation of function
# function1()

# this will print the docstring of the function
# print(function1.__doc__)
# print(print.__doc__)

# parameterless function
# - function that accepts no parameters
def function2():
    """parameterless function"""
    print("inside function2")

# function call
# function2()

# parameterized function
# - accepts at least one parameter
# - it is mandatory to pass the same number of arguments as number of parameter
# - parameter
#   - placeholder used while declaring a function
#   - also known as formal parameter
#   - def function3(p1): here p1 is a parameter
# - argument
#   - the value passed at the time of calling the function
#   - also known as actual parameter
#   - function3(10): here 10 is an argument

def function3(p1):
    """parameterized function"""
    print("inside function3")
    print(f"p1 = {p1}, type = {type(p1)}")

# call function3
# function3(10)
# function3("test")
# function3(True)

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

def function4(p1, p2, p3):
    """"""
    print("inside function4")
    print(f"p1 = {p1}, p2 = {p2}, p3 = {p3}")

# positional arguments
# - call the function by passing the arguments in the order of parameter
# - here value 10 will be given to p1, 20 to p2 and 30 to p3
# function4(10, 20, 30)

# since the order is important the values will not be assigned to expected parameter
# p1=30, p2=10, p3=20 <- this is wrong as the expectation was p1=10, p2=20, p3=30
# function4(30, 10, 20)

# keyword arguments (named arguments)
# function4(p1=10, p2=20, p3=30)

# since the arguments are passed along with their respective parameter, 
# the order of the arguments is not important
# function4(p3=30, p2=20, p1=10)

# arguments with different data types can be passed to a function
# function4(p1=10, p2="test", p3=True)

# combination of positional and keyword arguments
# function4(10, 20, p3=30)

# below line will generate an error 
# since the p1 parameter's value is passed twice (once with positional and second time with keyword)
# function4(10, 20, p1=30, p3=40)

# below line will generate a compile time error 
# since the keyword argument is passed before the positional ones
# function4(p1=10, 20, 30)

# by default all parameters are mandatory
# below line will generate an error as values for p2 and p3 are missing
# function4(p1=10)


# since one parameter (r) has default value,
# it becomes optional (caller may pass that argument)
def calculate_interest(p, n, r=7):
    """this function calculates interest"""
    print("inside calculate_interest function")
    print(f"p={p}, n={n}, r={r}")

    interest = (p * n * r) / 100
    print(f"interest = {interest}")

# since r is not passed, it will be taken from default value (7)
# calculate_interest(1000, 5)

# since r is passed as 6, it will be taken from argument (6)
# calculate_interest(800000, 18, 6)
# calculate_interest(800000, 18, r=6)
# calculate_interest(800000, 18, r=6.5)

def can_vote(age):
    if age >= 18:
        print("yes, person is eligible")
    else:
        print("no, person is NOT eligible")

# can_vote(15)
# can_vote(age=20)
# can_vote(age=45)

# get the age input from user
age = int(input("enter your age: "))
can_vote(age)