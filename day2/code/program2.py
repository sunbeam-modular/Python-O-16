# data types in python are inferred
# - automatically assigned by python by using its literal
# - developer CAN NOT assign the data type to a variable

# f"" => formatted string
# - a string which can take variable values inside it
# - {} used to get value of a variable or return value of a function

# numeric type 

# integer variable (does not have any decimal point)
num1 = 20
print(f"num1 = {num1}, type = {type(num1)}")

num2 = 100
print(f"num2 = {num2}, type = {type(num2)}")

# float variable (which has decimal point)
salary = 15.50
print(f"salary = {salary}, type = {type(salary)}")

# complex variable 
# - contains real and imaginary values
complex_value = 10 + 5j
print(f"complex_value = {complex_value}, type = {type(complex_value)}")

# string type
# - sequence of characters
# - both ' or " are used to declare a single line string
# - both ''' or """ are used to declare a multi line string

first_name = 'john'
print(f"first_name = {first_name}, type = {type(first_name)}")

last_name = "doe"
print(f"last_name = {last_name}, type = {type(last_name)}")

present_address = """105, 
nanded city,
sinhgad road,
pune"""
print(f"present_address = {present_address}, type = {type(present_address)}")

office_address = '''Sunbeam IT Park,
Hinjawadi'''
print(f"office_address = {office_address}, type = {type(office_address)}")

# single line string
permanant_address = "105," \
"nanded city," \
"sinhgad road," \
"pune"
print(f"permanant address = {permanant_address}, type = {type(permanant_address)}")

# boolean type

can_vote = True
print(f"can_vote = {can_vote}, type = {type(can_vote)}")

are_you_crazy = False
print(f"are_you_crazy = {are_you_crazy}, type = {type(are_you_crazy)}")


# special type (None)

my_var = None
print(f"my_var = {my_var}, type = {type(my_var)}")

# collection types

# list of values ([])
# - ordered mutable collection of values
numbers = [10, 20, 30, 40, 50]
print(f"numbers = {numbers}, type = {type(numbers)}")

languages = ["C", "C++", "Python", "C#"]
print(f"languages = {languages}, type = {type(languages)}")

# tuple of values (())
countries = ("india", "usa", "uk", "japan")
print(f"countries = {countries}, type = {type(countries)}")

# note:
# - here ordered means the insertion ordered

# tuple of prime numbers
# - ordered immutable collection of values
prime_numbers = (2, 3, 5, 7, 9, 11, 13, 17, 19)
print(f"prime_numbers = {prime_numbers}, type = {type(prime_numbers)}")

# set of values ({})
# - unordered collection of unique values
unique_values = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
print(f"unique_values = {unique_values}, type = {type(unique_values)}")

# dictionary of values ({})
# - collection of key-value pairs
error_codes = {"400": "Bad Request", "404": "Not Found", "401": "Unauthorized"}
print(f"error_codes = {error_codes}, type = {type(error_codes)}")