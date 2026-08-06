# int variables
n1, n2 = 10, 20
print(f"n1       = {n1}")
print(f"n2       = {n2}")

# while compilation, the compiler changes the + operator to
# n1.__add__(n2)
print(f"n1 + n2  = {n1 + n2}")
print(f"n1 + n2  = {n1.__add__(n2)}")

print(f"n1 - n2  = {n1 - n2}")
print(f"n1 / n2  = {n1 / n2}")
print(f"n1 * n2  = {n1 * n2}")
print("-" * 80)

s1, s2 = "hello", "world"

print(f"s1       = {s1}")
print(f"s2       = {s2}")

# while compilation, the compiler changes the + operator to
# s1.__add__(s2)
print(f"s1 + s2 = {s1 + s2}")
print(f"s1 + s2 = {s1.__add__(s2)}")
print("-" * 80)

class MyNumber:
    def __init__(self, number):
        self._number = number

    # override __str__() to print the details properly on console
    def __str__(self):
        return f"MyNumber [number={self._number}]"

    # add support to overload + operator
    def __add__(self, other):
        # print("__add__ called")
        return MyNumber(self._number + other._number)

    # add support to overload - operator
    def __sub__(self, other):
        return MyNumber(self._number - other._number)

    # add support to overload * operator
    def __mul__(self, other):
        return MyNumber(self._number * other._number)

    # add support to overload / operator
    def __truediv__(self, other):
        return MyNumber(self._number / other._number)

    # add support to overload // operator
    def __floordiv__(self, other):
        return MyNumber(self._number // other._number)

    # add support to overload % operator
    def __mod__(self, other):
        return MyNumber(self._number % other._number)

    # add support to overload == operator
    def __eq__(self, other):
        return self._number == other._number

    # add support to overload != operator
    def __ne__(self, other):
        return self._number != other._number

    # add support to overload > operator
    def __gt__(self, other):
        return self._number > other._number

    # add support to overload < operator
    def __lt__(self, other):
        return self._number < other._number

    # add support to overload >= operator
    def __ge__(self, other):
        return self._number >= other._number

    # add support to overload <= operator
    def __le__(self, other):
        return self._number <= other._number
    


p1, p2 = MyNumber(10), MyNumber(20)
print(f"p1       = {p1}")
print(f"p2       = {p2}")

# while compilation, the compiler changes the + operator to
# p1.__add__(p2)
print(f"p1 + p2  = {p1 + p2}")
print(f"p1 - p2  = {p1 - p2}")
print(f"p1 * p2  = {p1 * p2}")
print(f"p1 / p2  = {p1 / p2}")
print(f"p1 // p2 = {p1 // p2}")

# p1.__mod__(p2)
print(f"p1 % p2  = {p1 % p2}")

print(f"p1 == p2 = {p1 == p2}")
print(f"p1 != p2 = {p1 != p2}")
print(f"p1 >  p2 = {p1 > p2}")
print(f"p1 <  p2 = {p1 < p2}")
print(f"p1 >= p2 = {p1 >= p2}")
print(f"p1 <= p2 = {p1 <= p2}")