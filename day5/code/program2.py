# nested function
# - function declared within another function
# - also known as inner or local function
# - can not be accessed/called outside outer function
# - can access all the members of outer function
# - but the outer function can NOT access any member of inner function

# declare a variable 
num = 200
# print(f"num = {num}, type = {type(num)}")
# print()

# declare a function
# - by default a reference will be declared 
#   having same name as that of the function
# - the function body get compiled to byte codes
# - a new memory will be allocated to store these byte codes
# - the new memory's address will be kept in the function reference
# - function is considered as first class citizen
#   - in python, when a function is declared it will be treated as a variable of type function
def function1():
    print("inside function1")

# get the details of the function1 reference
# print(f"function1 = {function1}, type = {type(function1)}")

# call the function
# function1()

def function2():
    print("inside function2")

    # declare a local variable
    # scope: local
    my_var = 200
    print(f"my_var = {my_var}")

    # a new variable of type function will be declared here
    # scope: local
    def local_function():
        print("inside local_function")

    # make a call to the nest function
    local_function()

# function2()

# since my_var is local variable of function2, 
# it can NOT be accessed outside function2
# print(f"my_var = {my_var}")

# since local_function is a local/inner/nested function of function2
# it can NOT be called outside function2
# local_function()


def outer(p1: int):
    print("inside outer function")
    print(f"p1 = {p1}")

    # declare a local variable
    my_var = 100
    print(f"my_var = {my_var}")

    def inner_function1():
        print("inside inner_function1")

        # try accessing outer function's members
        print(f"p1 = {p1}")
        print(f"my_var = {my_var}")

        # declare a local variable
        inner_local_variable = 600
        print(f"inner_local_variable = {inner_local_variable}")

    inner_function1()

    # try accessing the inner function's member in outer function
    # since inner_local_variable is local to the inner, the outer function can NOT access it
    # print(f"inner_local_variable = {inner_local_variable}")

outer(p1=500)