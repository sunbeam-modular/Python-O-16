# package
# - collection of modules
# - types
#   - built-in packages
#     - math, josn, csv, os, re etc.
#     - installed by default when python gets installed
#   - third party packages
#     - numpy, pandas, matplotlib, seaborn, plotly, selenium etc.
#     - must be installed using any of the package managers

# import math module
import math

def function1():
    # load the constants 
    print(f"pi  = {math.pi}")
    print(f"e   = {math.e}")

    # infinity
    print(f"inf = {math.inf}")

    # Nan = not a number
    print(f"nan = {math.nan}")

# function1()


def function2():
    # power function
    print(f"3rd power of 5     = {math.pow(5, 3)}")
    print(f"3rd power of 5     = {5 ** 3}")
    print('-' * 80)

    print(f"square root of 100 = {math.sqrt(100)}")
    print(f"square root of 100 = {100 ** 0.5}")

# function2()

def function3():
    # get the floor of a float value
    print(f"floor value of 4.567 = {math.floor(4.567)}")

    # get factorial of a number
    # n! = n * n-1 * n-2 * .. * 1

    # 5 * 4 * 3 * 2 * 1
    print(f"factorial of 5       = {math.factorial(5)}")

    # get log of a number
    print(f"log of 10            = {math.log(10)}")
    print(f"log of 10            = {math.log10(10)}")

# function3()
