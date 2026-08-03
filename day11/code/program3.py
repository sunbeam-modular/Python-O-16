# string formatting
# - string aligment
#   - ljust(): justify (align) the string from left side
#   - rjust(): justify (align) the string from right side
#   - center(): justify (align) the string from center
# - string building
#   - format(): used to generate a new string using variable values

def function1():
    # string
    name = "sunbeam"
    print(f"name           = {name}")
    print(f"left aligned   = {name.ljust(15)}")
    print(f"right aligned  = {name.rjust(15)}")
    print(f"center aligned = {name.center(15)}")

# function1()

def function2():
    # string
    first_name = "john"
    last_name = "doe"

    # build a string with first name and last name
    print("first name = {}, last name = {}".format(first_name, last_name))
    print("first name = {0}, last name = {1}".format(first_name, last_name))
    print("first name = {1}, last name = {0}".format(last_name, first_name))
    print('-' * 80)

    print("first name = %s, last name = %s" % (first_name, last_name))
    print('-' * 80)

    print(f"first name = {first_name}, last name = {last_name}")

# function2()

def function3():
    # string
    first_name = "john"
    last_name = "doe"

    # left aligned string
    print(f"first name = {first_name:<15}, last_name = {last_name:<15}")

    # right aligned string
    print(f"first name = {first_name:>15}, last_name = {last_name:>15}")

    # center aligned string
    print(f"first name = {first_name:^15}, last_name = {last_name:^15}")

# function3()

def function4():
    # list of cars
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
    
    # print the list of cars
    print(f"model - company - price - mileage - color - fuel type")
    for car in cars:
        print(f"{car['model']} - {car['price']} - {car['mileage']} - {car['color']} - {car['fuel_type']}")
    print('-' * 80)
    print()
    print()
    print()

    print('-' * 55)
    print(f"| {'model':<10} | {'price':<6} | {'mileage':<7} | {'color':<6} | {'fuel type':<10} |")
    print('-' * 55)
    for car in cars:
        print(f"| {car['model']:<10} | {car['price']:<6} | {car['mileage']:<7} | {car['color']:<6} | {car['fuel_type']:<10} |")
    print('-' * 55)

# function4()

def function5():
    # integer
    number = 10

    print(f"number in decimal      = {number:d}")
    print(f"number in binary       = {number:b}")
    print(f"number in hexa-decimal = {number:x}")
    print(f"number in hexa-decimal = {number:X}")
    print(f"number in octal        = {number:o}")

# function5()

def function6():
    # float value
    number = 15.678232345

    print(f"number in float (all digits) = {number:f}")
    print(f"number in float (2 digits)   = {number:.2f}")
    print(f"number in float (3 digits)   = {number:.3f}")

# function6()