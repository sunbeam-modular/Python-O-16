# closure
# - calling inner function by remebering the outer function's member, outside
#   the outer function's scope
# - a function returning reference of inner function

def outer_function():
    print("inside the outer function")

    # local varible
    number = 100
    print(f"number = {number}")

    # nested/local/inner function
    def inner_function():
        print(f"inside the inner function")

        # inner function can access all the members of outer function
        print(f"number = {number}")

    # call inner function
    # inner_function()

    # return the inner function reference as return value of outer_function
    # by default function name is a function reference
    return inner_function
    
    # return value stored in varible number (100)
    # return number

# outer_function()

# since number is local variable of outer_function, it can NOT be access here
# print(f"number = {number}")

# since inner_function is a local or inner function of outer_function, it can NOT be called here
# inner_function()

# call the outer_function and capture the return value in return_value variable
return_value = outer_function()
print(f"return_value = {return_value}, type = {type(return_value)}")

# since outer_function is returning a function referece, make a call to the return_value
return_value()
