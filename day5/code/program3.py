# lambda function
# - anonymous function
# - must be declared using lambda keyword
# - must contain only one statement (expression) in its body
# - must not use return keyword
# - the expression's value will get returned implicitly
# - if the lambda does not have any expression, it returns the value as return value of body
# - does not support type hinting/type annotation
# - similar to inline function in C (faster than named function)
# - not all named functions can be converted into lambda,
#   but all lambda functions can be converted to named functions

# named function to get a square of a number
def fn_square(number: int):
    return number ** 2

print(f"square of 5 = {fn_square(5)}")
print(f"fn_square = {fn_square}, type = {type(fn_square)}")
print()

# lambda function to get a square of a number
lambda_square = lambda n: n ** 2
print(f"square of 5 = {lambda_square(5)}")
print(f"lambda_square = {lambda_square}, type = {type(lambda_square)}")
print()

# lambda to add two values
add = lambda p1, p2: p1 + p2
print(f"10 + 20 = {add(10, 20)}")

# lambda to calculate interest
calculate_simple_interest = lambda p, n, r: (p * n * r) / 100
print(f"simple interest = {calculate_simple_interest(10000, 5, 7.5)}")

# self invoking lambda function
# p1 * p2 -> 10 * 20
print((lambda p1, p2: p1 * p2) (10, 20))

# here since there is no expression in the body
# the lambda will return the return value of print function
# since the print() does not return anything, the lambda function
# here will return None
non_returning_lambda = lambda n: print(f"inside lambda n = {n}")
print(f"non_returning_lambda = {non_returning_lambda(10)}")
