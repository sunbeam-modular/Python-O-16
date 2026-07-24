# scope of variables
# - global
#   - by default variable declared outside of any function
#   - global variable can be accessed anywhere in code (inside or outside any function) only within the file
#   - global variables can not be updated within function accidently (by default)
#   - 
# - local
#   - variable declared inside a function
#   - local variable can be accessed only within the function in which it is declared
#   - function parameters and variables declared within the function by default are locally scopped

# scope: global

# using global keyword outside function is not required
# global num
num = 200
print(f"outside any function num = {num}")
print()

def function1():
    print("inside function1")

    # scope: local
    my_var = "my_var value"
    print(f"my_var = {my_var}")

    # update global variable and persist the change
    global num

    # change the value of global variable
    num = 400 

    # check if global variable can be accessed within a function
    print(f"num = {num}")

function1()
print()

# since my_var is local variable of function1, 
# it can not be accessed outside of function1
# print(f"outside function1, my_var = {my_var}")

print(f"outside any function num = {num}")


def function2():
    print("inside function2")

    # update glboally scopped variable
    global num
    num = 500

    print(f"num = {num}")

function2()
print()

print(f"outside any function num = {num}")

def function3():
    print("inside function3")

    # a new locally scopped variable will be declared
    # this variable will be accessible only within the function
    # once the function3 returns, this variable will be removed from memory
    num = 600
    print(f"num = {num}")

    # global keyword can also be used to declare a global variable within function
    global new_global_var
    new_global_var = 900

    print(f"new_global_var = {new_global_var}")

function3()
print()

print(f"outside function3, new_global_var = {new_global_var}")




