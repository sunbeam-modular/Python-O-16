# comprehension
# - simpler syntax used to combine the map and filter logic together
# - types
#   - list comprehension
#     - syntax:
#       - simulation of a map
#         - [<tmp var> for <tmp var> in <collection>]
#         - [<transformation logic on tmp var> for <tmp var> in <collection>]
#       - simulation of filter function
#         - [<tmp var> for <tmp var> in <collection> if <condition>]
#   - tuple comprehension
#   - dictionary comprehension

def function1():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"numbers  = {numbers}")

    # get square of every number
    squares = [number ** 2 for number in numbers]
    print(f"squares  = {squares}")

    # get cube of every number
    cubes = [n ** 3 for n in numbers]
    print(f"cubes    = {cubes}")

# function1()

def function2():
    # list of product prices
    prices = [100, 200, 150, 230, 280, 900, 500]
    print(f"prices            = {prices}")

    # get new prices after 10% discount
    discounted_prices = [price - (price / 10) for price in prices]
    print(f"discounted prices = {discounted_prices}")

# function2()

def function3():
    # list of names
    names = ['john', 'alice', 'bob', 'david', 'jane', 'ellik']  
    print(f"names   = {names}")

    # get the length of every name
    lengths = [len(name) for name in names]
    print(f"lengths = {lengths}")

# function3()

def function4():
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

    # get the list of models
    models = [car['model'] for car in cars]
    print(f"models = {models}")    

# function4()
