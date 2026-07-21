# statically typed language
# - the data type is assigned by developer at the time of compilation
# - compiler checks the data type and the value stored in the variable
# - e.g. c, c++, java
# - int num = 20;
# - num = 15.50; <- this will generate a compile time error

# dynamically typed language
# - the data type is inferred at the time of running the code (dynamically)
# - compiler does not check the value stored in the variable and data type of variable
# - e.g. python, JS
# - num = 20
# - num = 15.50

# int type
num = 100
print(f"num = {num}, type = {type(num)}")

# float type
num = 15.50
print(f"num = {num}, type = {type(num)}")

# string type
num = 'test'
print(f"num = {num}, type = {type(num)}")

# boolean type
num = True
print(f"num = {num}, type = {type(num)}")

# none type
num = None
print(f"num = {num}, type = {type(num)}")

# int type
num = 500
print(f"num = {num}, type = {type(num)}")

# list type
num = [10, 20, 30, 40, 50]
print(f"num = {num}, type = {type(num)}")

# tuple type
num = (10, 20, 30, 40, 50)
print(f"num = {num}, type = {type(num)}")