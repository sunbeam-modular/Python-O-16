# type conversion

# implicit type conversion
# - possible only when there is no loss of data
# - in the following example, value 10 gets converted to float
#   and float addition gets performed
addition = 10 + 15.50
print(f"addition = {addition}, type = {type(addition)}")


# explicit type conversion
# - many a times data gets lost
# - only when it is possible, the value gets converted to a valid value
#   otherwise, None will be given or an exception may get raised
# - in-built functions are used to convert data type
# - e.g.
#   - int(): used to convert anything to int 
#   - str(): used to convert anything to string
#   - bool(): used to convert anything to boolean
#   - float(): used to convert anything to float
#   - complex(): used to covert anything to complex
#   - list(): used to convery any collection to list
#   - tuple(): used to convery any collection to tuple
#   - set(): used to convery any collection to set
#   - dict(): used to convery any collection to dictionary

# convert a float value to int data type
salary = 15.50
salary_int_value = int(salary)
print(f"salary = {salary}, type = {type(salary)}")
print(f"salary_int_value = {salary_int_value}, type = {type(salary_int_value)}")

# convert a string value to int data type
str_value = "10"
str_value_in_int = int(str_value)
print(f"str_value = {str_value}, type = {type(str_value)}")
print(f"str_value_in_int = {str_value_in_int}, type = {type(str_value_in_int)}")

# this is not valid conversion as "sunbeam" can not be converted to int
# thats the reason the application will crassh with an error ValueError (exception)
# str_value = "sunbeam"
# str_value_in_int = int(str_value)

# convert None to boolean -> False
print(f"value None in boolean = {bool(None)}")

# convert int to boolean
# - only 0 gets converted to False
# - rest of the values get converted to True
print(f"value 1 in boolean = {bool(1)}")
print(f"value 0 in boolean = {bool(0)}")
print(f"value -1 in boolean = {bool(-1)}")
print(f"value 100 in boolean = {bool(100)}")

# convert float to boolean
# - only 0.0 gets converted to False
# - rest of the values get converted to True
print(f"value 15.50 in boolean = {bool(15.50)}")
print(f"value 0.0 in boolean = {bool(0.0)}")

# convert string to boolean
# - only empty string gets converted to False
# - non-empty strings get converted to True
print(f"value 'True' in boolean = {bool('True')}")
print(f"value 'False' in boolean = {bool('False')}")
print(f"value '' in boolean = {bool('')}")