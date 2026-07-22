# logical (boolean) operators
# - the operation will be performed on boolean operands
# - if the operand is not boolean, it will get converted into boolean first

# logical and operator
# - if the first condition is False the second condition will not be checked
print(f"True and True   = {True and True}")
print(f"True and False  = {True and False}")
print(f"False and True  = {False and True}")
print(f"False and False = {False and False}")

print()

# logical or operator
# - even if the first condition is false the second condition will be checked
# - if the first condition is True the second condition will not be checked
print(f"True or True   = {True or True}")
print(f"True or False  = {True or False}")
print(f"False or True  = {False or True}")
print(f"False or False = {False or False}")

print()

# logical not operator
print(f"not True   = {not True}")
print(f"not False  = {not False}")

print()

print(f"10 and 5 = {10 and 5}")
print(f"10 and 0 = {10 and 0}")
print(f"0 and 5 = {0 and 5}")