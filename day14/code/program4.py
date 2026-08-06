# class Car:
# class Car():
class Car(object):
    def __init__(self, model, company):
        self._model = model
        self._company = company

    # overriding the __str__ method to print the car details properly on console
    def __str__(self):
        return f"Car [model={self._model}, company={self._company}]"

# create an object of Car class
car = Car("triber", "renault")

# create a number variable
num = 200

print(f"base class of Car = {Car.__base__}")
print(f"num = {num}")
print(f"num = {num.__str__()}")

# by default to print the car object on console, compiler call __str__() on car object
print(f"car = {car}")
print(f"car = {car.__str__()}")

# car.display()