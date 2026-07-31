# functional programming
# - function is a first class citizen
#   - variable can be created of type function
# - a function can be passed as an argument to another function
# - a function can be returned as a return value from a function
# - built in functions
#   - map()
#     - used to transform the values from a collection
#     - it is a lazy function: returns values only when required
#     - performs better than writing transformation logic
#     - always returns a collection with same length as that of the original one
#     - param1: reference to a function or lambda
#     - param2: collection
#   - filter()


def function1():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"numbers = {numbers}")

    # get square of every number in numbers list and store in another list
    squares = []

    # iterate over numbers list
    for number in numbers:
        # get the square of every number
        square = number ** 2

        # append to the squares list
        squares.append(square)

    print(f"squares = {squares}")

# function1()

def add():
    print(f"10 + 20 = {10 + 20}")

def subtract(p1, p2):
    print(f"subtraction = {p1 - p2}")

def function2(func, func_params):
    print(f"inside a function2")
    print(f"func = {func}, type = {type(func)}")

    # call the function func is referencing
    func(**func_params)

# passing an integer
# function2(10)

# passing a string
# function2("test")

# passing a function1 as function reference to the function2
# function2(function1)

# passing add function reference
# function2(add, {})

# passing subtract function reference
# function2(subtract, {'p1': 10, 'p2': 5})

def function3(p1, p2, p3):
    print(f"inside function3")
    print(f"p1 = {p1}, p2 = {p2}, p3 = {p3}")

# positional arguments
# n1 = input("enter value1: ")
# n2 = input("enter value2: ")
# n3 = input("enter value3: ")
# function3(n1, n2, n3)

# positional arguments
# function3(10, 20, 30)

# keyword arguments
# function3(p1=10, p2=20, p3=30)

# list of values
# values = [10, 20, 30]

# splat operator
# - extract values from list and pass them as positional arguments
# function3(10, 20, 30)
# function3(*values)

# dictionary of values
# arguments_dictionary = {'p1': 10, 'p2': 20, 'p3': 30}

# splat operator
# - extract the key-value pairs and pass them as keyword arguments
# function3(p1=10, p2=20, p3=30)
# function3(**arguments_dictionary)

def function4():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"numbers = {numbers}")

    # create a lambda to get the square of a number
    square = lambda n: n ** 2

    # collect all the squares
    squares = []

    for number in numbers:
        # get square of every number and append to the squares list
        squares.append(square(number))

    print(f"squares = {squares}")

# function4()

def function5():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"numbers = {numbers}")

    # define lambda to get transformed value
    square = lambda n: n ** 2

    # transform the values to their squares
    squares = list(map(square, numbers))
    print(f"squares = {squares}")

# function5()

def function6():
    # list of product prices
    prices = [100, 200, 150, 230, 280, 900, 500]

    # requirement: calculate new prices by having discount of 10%

    # define the logic of transformation
    calculate_discounted_price = lambda p: p - (p / 10)

    # collect all new prices
    discounted_prices = []

    # calculate all discounted prices
    for price in prices:
        # calculate discounted price
        discounted_price = calculate_discounted_price(price)

        # collect the new price
        discounted_prices.append(discounted_price)

    print(f"original prices   = {prices}")
    print(f"discounted prices = {discounted_prices}")

# function6()

def function7():
    # list of product prices
    prices = [100, 200, 150, 230, 280, 900, 500]

    # requirement: calculate new prices by having discount of 10%

    # define the logic of transformation
    calculate_discounted_price = lambda p: p - (p / 10)

    # get all discounted prices
    discounted_prices = list(map(calculate_discounted_price, prices))

    print(f"original prices   = {prices}")
    print(f"discounted prices = {discounted_prices}")

# function7()

def function8():
    # list of names
    names = ['john', 'alice', 'bob', 'david', 'jane', 'ellik']  
    print(f"names   = {names}")

    # define lambda to transform name into its length
    # get_length = lambda name: len(name)
    
    def get_length(name):
        return len(name)

    # get the length of every name
    lengths = list(map(get_length, names))
    print(f"lengths = {lengths}")

# function8()

def function9():
    # list of dictionaries
    cars = [
        {
            "model": "Civic",
            "company": "Honda",
            "price": 20000,
            "mileage": 50000,
            "color": "Blue",
            "fuel_type": "Gasoline"
        },
        {
            "model": "Corolla",
            "company": "Toyota",
            "price": 22000,
            "mileage": 30000,
            "color": "White",
            "fuel_type": "Hybrid"
        },
        {
            "model": "Camry",
            "company": "Toyota",
            "price": 25000,
            "mileage": 20000,
            "color": "Black",
            "fuel_type": "Gasoline"
        },
        {
            "model": "Accord",
            "company": "Honda",
            "price": 23000,
            "mileage": 40000,
            "color": "Red",
            "fuel_type": "Hybrid"
        },
        {
            "model": "Elantra",
            "company": "Hyundai",
            "price": 18000,
            "mileage": 60000,
            "color": "Silver",
            "fuel_type": "Gasoline"
        },
        {
            "model": "Altima",
            "company": "Nissan",
            "price": 24000,
            "mileage": 50000,
            "color": "Gray",
            "fuel_type": "Hybrid"
        },
        {
            "model": "Focus",
            "company": "Ford",
            "price": 20000,
            "mileage": 30000,
            "color": "Blue",
            "fuel_type": "Gasoline"
        },
        {
            "model": "Sentra",
            "company": "Nissan",
            "price": 22000,
            "mileage": 40000,
            "color": "White",
            "fuel_type": "Hybrid"
        },
        {
            "model": "CR-V",
            "company": "Honda",
            "price": 28000,
            "mileage": 20000,
            "color": "Black",
            "fuel_type": "Gasoline"
        },
        {
            "model": "Rav4",
            "company": "Toyota",
            "price": 30000,
            "mileage": 60000,
            "color": "Red",
            "fuel_type": "Hybrid"
        }
    ]

    # transformation logic: transform every car dictionary to its model
    get_model = lambda car: car['model']

    # get all models from the cars collection
    models = list(map(get_model, cars))

    print(f"cars = {cars}")
    print('-' * 80)
    print(f"models = {models}")

# function9() 
