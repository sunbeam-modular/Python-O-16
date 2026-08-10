import numpy as np

def function1():
    # array of numbers
    numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print(f"numbers     = {numbers}")
    print('-' * 80)

    # positive indexing
    print(f"numbers[0]  = {numbers[0]}")
    print(f"numbers[1]  = {numbers[1]}")
    print(f"numbers[2]  = {numbers[2]}")
    print(f"numbers[3]  = {numbers[3]}")
    print(f"numbers[4]  = {numbers[4]}")
    print('-' * 80)

    # negative indexing
    print(f"numbers[-1] = {numbers[-1]}")
    print(f"numbers[-2] = {numbers[-2]}")
    print(f"numbers[-3] = {numbers[-3]}")
    print(f"numbers[-4] = {numbers[-4]}")
    print(f"numbers[-5] = {numbers[-5]}")

# function1()

def function2():
    # array of numbers
    numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print(f"numbers                  = {numbers}")
    print('-' * 80)

    # multiple values indexing
    print(f"numbers[[0, 1, 5, 8, 7]] = {numbers[[0, 1, 5, 8, 7]]}")
    print(f"numbers[[3, 6]]          = {numbers[[3, 6]]}")
    print(f"numbers[[-3, -6]]        = {numbers[[-3, -6]]}")
    print(f"numbers[[3, -6]]         = {numbers[[3, -6]]}")

# function2()

def function3():
    # array of numbers
    numbers = np.array([10, 20, 30, 40, 50])
    print(f"numbers                  = {numbers}")
    print('-' * 80)

    # boolean indexing
    # - get the values at the True positions
    print(f"numbers[[T, F, T, F, T]] = {numbers[[True, False, True, False, True]]}")
    print(f"numbers[[F, T, F, T, F]] = {numbers[[False, True, False, True, False]]}")

# function3()

def function4():
    # array of numbers
    numbers = np.array([10, 20, 30, 40, 50])
    print(f"numbers         = {numbers}")
    print('-' * 80)

    # broadcast operation
    # - performing an operation on every member of an array
    
    # arithmetic operations
    print(f"numbers + 40    = {numbers + 40}")
    print(f"numbers - 40    = {numbers - 40}")
    print(f"numbers / 40    = {numbers / 40}")
    print(f"numbers // 40   = {numbers // 40}")
    print(f"numbers * 40    = {numbers * 40}")
    print(f"numbers * 2     = {numbers * 2}")
    print('-' * 80)

    # comparison operations
    print(f"numbers == 40   = {numbers == 40}")
    print(f"numbers != 40   = {numbers != 40}")
    print(f"numbers > 40    = {numbers > 40}")
    print(f"numbers >= 40   = {numbers >= 40}")
    print(f"numbers < 40    = {numbers < 40}")
    print(f"numbers <= 40   = {numbers <= 40}")

# function4()

def function5():
    # array of numbers
    numbers = np.array([10, 20, 30, 40, 50])
    print(f"numbers                  = {numbers}")
    print('-' * 80)

    # filtering array
    print(f"number > 20              = {numbers > 20}")
    print(f"numbers[number > 20]     = {numbers[numbers > 20]}")
    print(f"numbers[number < 40]     = {numbers[numbers < 40]}")

function5()