# bitwise operators

# int values
n1 = 5
n2 = 8

# print the binary values 
print(f"{n1} in binary = {bin(n1)}")
print(f"{n2} in binary = {bin(n2)}")

print()

# bitwise and operator (&)
print(f"{n1}[{bin(n1)}] & {n2}[{bin(n2)}] = {n1 & n2}[{bin(n1 & n2)}]")

# bitwise or operator (|)
print(f"{n1}[{bin(n1)}] | {n2}[{bin(n2)}] = {n1 | n2}[{bin(n1 | n2)}]")

# bitwise not operator (~)
print(f"~{n1}[{bin(n1)}] = {~n1}[{bin(~n1)}]")

# bitwise xor operator (^)
print(f"{n1}[{bin(n1)}] ^ {n2}[{bin(n2)}] = {n1 ^ n2}[{bin(n1 ^ n2)}]")

print()

# bitwise left shift operator
# - preferred over multiplication with power of 2 as it is faster than the respective multiplication
#   - prefer 5 << 3 instead 5 * 8
# - preferred in system level programming
# - answer will be calculated with formula
#   - number << n = number * 2 ^ n

# 5 * 2^1 = 5 * 2 = 10
print(f"{n1}[{bin(n1)}] << 1 = {n1 << 1}[{bin(n1 << 1)}]")

# 5 * 2^2 = 5 * 4 = 20
print(f"{n1}[{bin(n1)}] << 2 = {n1 << 2}[{bin(n1 << 2)}]")

# 5 * 2^3 = 5 * 8 = 40
print(f"{n1}[{bin(n1)}] << 3 = {n1 << 3}[{bin(n1 << 3)}]")

# 5 * 2^4 = 5 * 16 = 80
print(f"{n1}[{bin(n1)}] << 4 = {n1 << 4}[{bin(n1 << 4)}]")

print()

# bitwise right shift operator
# - preferred over division with power of 2 as it is faster than the respective division
#   - prefer 5 >> 3 instead 5 / 8
# - preferred in system level programming
# - answer will be calculated with formula
#   - number >> n = number * 2 ^ n

# 5 / 2^1 = 5 / 2 = 2
print(f"{n1}[{bin(n1)}] >> 1 = {n1 >> 1}[{bin(n1 >> 1)}]")

# 5 / 2^2 = 5 / 4 = 1
print(f"{n1}[{bin(n1)}] >> 2 = {n1 >> 2}[{bin(n1 >> 2)}]")