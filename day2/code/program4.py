# type hinting
# - declaring a variable with a hint
# - is optional
# - the hint is not going to mandate the variable data type
# - in other words, the data type of a variable is decided 
#   by the value stored inside it
# - the type hinting is used by the developers to understand the code
#   or by the IDEs to show warning when required

# int is a hint given to the developer
num: int = 20
print(f"num = {num}, type = {type(num)}")

# though the hint suggest salary is of str type
# the actual data type of salary will be decided by the value (15.50 - float)
salary: str = 15.50
print(f"salary = {salary}, type = {type(salary)}")