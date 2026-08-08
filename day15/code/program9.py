# not recommended
# - imports everything from math_operations
# from math_operations import *

def function1():
    # import module math_operations
    import math_operations

    # access the entities from math_operations
    math_operations.add(10, 20)
    math_operations.subtract(10, 20)
    math_operations.divide(10, 20)
    math_operations.multiply(10, 20)

    # access the constants/variables
    print(f"PI = {math_operations.PI}")

    # create an object of Math class
    math = math_operations.Math()
    print(f"math = {math}")

# function1()

    
def function2():
    # import module math_operations with an alias (mo)
    import math_operations as mo

    # access the entities from math_operations
    mo.add(10, 20)
    mo.subtract(10, 20)
    mo.divide(10, 20)
    mo.multiply(10, 20)

    # access the constants/variables
    print(f"PI = {mo.PI}")

    # create an object of Math class
    math = mo.Math()
    print(f"math = {math}")

# function2()

def function3():
    # import required members from the module
    from math_operations import add, subtract, PI

    # since the add and subtract functions are imported from math_operations module
    # the following statements will call the functions defined in the module
    add(10, 20)
    subtract(10, 20)
    print(f"PI = {PI}")

# function3()

def function4():
    # import required members from the module
    from math_operations import add as my_add

    # since the add and subtract functions are imported from math_operations module
    # the following statements will call the functions defined in the module
    my_add(10, 20)

function4()

def function5():
    import math_operations

    # get the module path
    print(f"math_operations: {math_operations}")

    # get the collection of the members
    # print(math_operations.__dir__())
    print(dir(math_operations))

    # get the name of the module
    print(math_operations.__name__)

# function5()