import random

def function1():
    # generate a random number
    print(f"random number between 1 to 10 = {random.randint(1, 10)}")

    # get a random number from a range
    print(f"random number between 1 to 10 = {random.randrange(1, 10, 2)}")

# function1() 

def function2():
    # generate random number using a distribution
    print(f"random number between 1 to 10 = {random.uniform(1, 10)}")

# function2()

def function3():
    # create a colors list
    colors = ['red', 'blue', 'green', 'black', 'white', 'yellow', 'magenta']

    # select a color randomly from the given colors list
    print(f"random color = {random.choice(colors)}")

# function3()