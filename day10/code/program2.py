# filter()
# - used to filter the collection based on certain criteria (condition)
# - iterates over the collection, check if every value satisfies the criteria
# - the values which satisfy the criteria, will get returned in a collection
# - returns a collection with either same length or smaller length as that of the original collection

def function1():
    # list of numbers
    numbers = [10, 39, 89, 71, 82, 45, 38, 19, 17, 49]
    print(f"numbers      = {numbers}")

    # collect all even numbers
    even_numbers = []

    # requirement: find all even numbers
    for number in numbers:

        # check if the number is even
        if number % 2 == 0:
            # collect the even number
            even_numbers.append(number) 

    print(f"even numbers = {even_numbers}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 39, 89, 71, 82, 45, 38, 19, 17, 49]
    print(f"numbers      = {numbers}")

    # collect all even numbers
    even_numbers = []

    # create lambda to check if the number is even
    is_even = lambda n: n % 2 == 0

    # requirement: find all even numbers
    for number in numbers:

        # check if the number is even
        if is_even(number):

            # collect the even number
            even_numbers.append(number) 

    print(f"even numbers = {even_numbers}")

# function2()

def function3():
    # list of numbers
    numbers = [10, 39, 89, 71, 82, 45, 38, 19, 17, 49]
    print(f"numbers      = {numbers}")

    # create lambda to check if the number is even
    is_even = lambda n: n % 2 == 0

    # create a lambda to check if the number is odd
    is_odd = lambda n: n % 2 != 0

    # get the list of even numbers
    even_numbers = list(filter(is_even, numbers))
    print(f"even numbers = {even_numbers}")

    # get the list of odd numbers
    odd_numbers = list(filter(is_odd, numbers))
    print(f"odd numbers  = {odd_numbers}")

# function3()

def function4():
    # list of emails
    emails = ['amit@test.com', 'johnexample.com', 'jane@ms.com', 'tim@apple.com']
    print(f"emails        = {emails}")

    # invalid email: email which does not contain @ symbol
    is_invalid_email = lambda e: '@' not in e

    # find invalid emails 
    invalid_emails = list(filter(is_invalid_email, emails))
    print(f"invalid emails = {invalid_emails}")

# function4()

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

    # check if a car is affordable
    is_affordable = lambda car: car['price'] <= 20000

    # find affordable cars (price <= 20000)
    affordable_cars = list(filter(is_affordable, cars))
    print(f"affordable cars = {affordable_cars}")

    # check if a car is hybrid
    is_hybrid = lambda car: car['fuel_type'] == 'Hybrid'

    # find all hybrid cars
    hybrid_cars = list(filter(is_hybrid, cars))
    print(f"hybrid cars     = {hybrid_cars}")

# function9()

def function10():
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

    # check if a car is hybrid
    is_hybrid = lambda car: car['fuel_type'] == 'Hybrid'

    # find all hybrid cars
    hybrid_cars = list(filter(is_hybrid, cars))
    print(f"hybrid cars     = {hybrid_cars}")

    # transformation logic: transform every car dictionary to its model
    get_model = lambda car: car['model']

    # find the models of hybrid cars
    hybrid_car_models = list(map(get_model, hybrid_cars))
    print(f"hybrid car models = {hybrid_car_models}")

# function10()

def function11():
    # list of numbers
    numbers = [10, 39, 89, 71, 82, 45, 38, 19, 17, 49]
    print(f"numbers             = {numbers}")

    # create lambda to check if the number is even
    is_even = lambda n: n % 2 == 0

    # get the list of even numbers
    even_numbers = list(filter(is_even, numbers))
    print(f"even numbers        = {even_numbers}")

    # create a lambda to get the square of a number
    square = lambda n: n ** 2

    # find square of even numbers
    even_number_squares = list(map(square, even_numbers))
    print(f"even number squares = {even_number_squares}")

# function11()