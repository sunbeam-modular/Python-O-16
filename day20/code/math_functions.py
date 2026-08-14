def add(p1, p2):
    return p1 + p2

def subtract(p1, p2):
    return p1 - p2

def divide(p1, p2):
    return p1 / p2

def multiply(p1, p2):
    return p1 * p2

def is_prime(number):
    if number == 1: return True
    elif number == 2: return True
    else:
        for i in range(2, number - 1):
            if number % i == 0:
                return False

        return True

# print(f"is 4 prime : {is_prime(4)}")
# print(f"is 7 prime : {is_prime(7)}")
# print(f"is 11 prime: {is_prime(11)}")
# print(f"is 13 prime: {is_prime(13)}")
# print(f"is 17 prime: {is_prime(17)}")
# print(f"is 15 prime: {is_prime(15)}")