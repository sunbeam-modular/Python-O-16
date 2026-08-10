import numpy as np

def function1():
    # create a list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}, {type(numbers)}")

    # create an array
    array = np.array([10, 20, 30, 40])
    print(f"array   = {array}, type = {type(array)}")

# function1()

def print_array_info(array):
    print(f"array                           = {array}")
    print(f"type                            = {type(array)}")
    print(f"#dimensions                     = {array.ndim}")
    print(f"length                          = {array.size}")

    # get the data type of every item
    print(f"type of item                    = {array.dtype}")

    # get the memory required to store every item
    print(f"memory required for every item  = {array.itemsize} bytes")

    # get the total memory required to store the entire array
    print(f"total memory required for array = {array.itemsize * array.size} bytes")
    print(f"total memory required for array = {array.nbytes} bytes")

    # get the shape of an array
    print(f"shape of array                  = {array.shape}")

    # get the flags
    print(f"flags                           = {array.flags}")

def function2():
    # create 1d array
    array1 = np.array([10, 20, 30, 40, 50])
    print_array_info(array1)
    print('-' * 80)

    # create 2d array
    array2 = np.array([
        [10, 20], 
        [30, 40], 
        [50, 60]
    ])
    print_array_info(array2)
    print('-' * 80)

    # create 3d array
    array3 = np.array([
        [
            [10, 20],
            [30, 40]
        ],
        [
            [50, 60],
            [70, 80]
        ]
    ])
    print_array_info(array3)

# function2()

def function3():
    # create 1d array
    array1 = np.array([10, 20, 30, 40, 50])
    print_array_info(array1)
    print('-' * 80)    

    # create 1d array
    array2 = np.array([10, 20, 30, 40, 50], dtype=np.int32)
    print_array_info(array2)
    print('-' * 80)    

    # create 1d array
    array3 = np.array([10, 20, 30, 40, 50], dtype=np.int16)
    print_array_info(array3)
    print('-' * 80)    

    # create 1d array
    array4 = np.array([10, 20, 30, 40, 50], dtype=np.int8)
    print_array_info(array4)
    print('-' * 80)    

# function3()

def function4():
    # create a 1d array with all zeros
    array1 = np.zeros(5)
    print_array_info(array1)
    print('-' * 80)

    # create a 2d array with all zeros
    array2 = np.zeros((3, 5))
    print_array_info(array2)
    print('-' * 80)

    # create a 1d array with all zeros
    array3 = np.zeros(5, dtype=np.int8)
    print_array_info(array3)
    print('-' * 80)

# function4()

def function5():
    # create a 1d array with all zeros
    array1 = np.ones(5)
    print_array_info(array1)
    print('-' * 80)

    # create a 2d array with all zeros
    array2 = np.ones((3, 5))
    print_array_info(array2)
    print('-' * 80)

    # create a 2d array with all zeros
    array3 = np.ones((3, 5), dtype=np.int8)
    print_array_info(array3)
    print('-' * 80)

# function5()

def function6():
    # create a 1d array with random values
    array1 = np.random.randint(1, 10, 10)
    print_array_info(array1)
    print('-' * 80)

    # create a 1d array with random values
    array2 = np.random.randint(1, 10, (5, 3))
    print_array_info(array2)
    print('-' * 80)

# function6()

def function7():
    # create an 1d array 
    array1 = np.array([10, 20, 30, 40, 50, 60])
    print_array_info(array1)
    print('-' * 80)

    # convert the array to another dimension
    array2 = array1.reshape((2, 3))
    print_array_info(array2)
    print('-' * 80)

    # convert the array to another dimension
    array3 = array1.reshape((3, 2))
    print_array_info(array3)
    print('-' * 80)

    # convert the array to another dimension
    array4 = array1.reshape((1, 6))
    print_array_info(array4)
    print('-' * 80)

    # convert the array to another dimension
    array5 = array1.reshape((6, 1))
    print_array_info(array5)
    print('-' * 80)

function7()