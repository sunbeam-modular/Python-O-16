import pandas as pd
import numpy as np

def function1():
    # list of numbers
    numbers_list = [10, 20, 30, 40, 50]
    print(f"numbers_list   = {numbers_list}, type = {type(numbers_list)}")

    # tuple of numbers
    numbers_tuple = 10, 20, 30, 40, 50
    print(f"numbers_tuple  = {numbers_tuple}, type = {type(numbers_tuple)}")

    # array of numbers
    numbers_array = np.array([10, 20, 30, 40, 50])
    print(f"numbers_array  = {numbers_array}, type = {type(numbers_array)}")

    # series of numbers
    numbers_series = pd.Series([10, 20, 30, 40, 50])
    print(f"numbers_series = {numbers_series}, type = {type(numbers_series)}")

# function1()

def function2():
    # create a series using list (sequence)
    numbers = pd.Series([10, 20, 30, 40, 50])
    print(numbers)
    print('-' * 80)

    # create series using tuple (sequence)
    numbers = pd.Series((10, 20, 30, 40, 50))
    print(numbers)
    print('-' * 80)

    # create series using a dictionary
    person = pd.Series({"name": "person1", "email": "person1@test.com", "address": "pune"})
    print(person)
    print('-' * 80)

    # create a series using set (unordered)
    # note: series can not be created using a set object
    # numbers = pd.Series({10, 20, 30, 40, 50})
    # print(numbers)
    # print('-' * 80)

# function2()

def function3():
    # create a series using list (sequence)
    numbers = pd.Series([10, 20, 30, 40, 50])
    print(numbers)
    print('-' * 80)

    print(f"values      = {numbers.values}")
    print(f"index       = {numbers.index}")
    print(f"shape       = {numbers.shape}")
    print(f"size        = {numbers.size}")
    print(f"data type   = {numbers.dtype}")
    print(f"#dimensions = {numbers.ndim}")

# function3()

def function4():
    # create a series using list (sequence) with different index positions
    numbers = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
    print(numbers)
    print('-' * 80)

    print(f"values      = {numbers.values}")
    print(f"index       = {numbers.index}")
    print(f"shape       = {numbers.shape}")
    print(f"size        = {numbers.size}")
    print(f"data type   = {numbers.dtype}")
    print(f"#dimensions = {numbers.ndim}")

# function4()

def function5():
    # create a series using list (sequence)
    numbers = pd.Series([10, 20, 30, 40, 50])
    print(numbers)
    print('-' * 80)

    # positive indexing 
    print(f"numbers[0] = {numbers[0]}")
    print(f"numbers[1] = {numbers[1]}")
    print(f"numbers[2] = {numbers[2]}")
    print(f"numbers[3] = {numbers[3]}")
    print(f"numbers[4] = {numbers[4]}")

    # negative indexing 
    # - since the -1 position does not exist, the following statement will raise error KeyError
    # print(f"numbers[-1] = {numbers[-1]}")

# function5()


def function6():
    # create a series using list (sequence)
    numbers = pd.Series([10, 20, 30, 40, 50], index=[-1, -2, -3, -4, -5])
    print(numbers)
    print('-' * 80)

    # positive indexing 
    # - since index 0 does not exist in numbers, following statement will raise KeyError
    # print(f"numbers[0] = {numbers[0]}")

    # negative indexing
    print(f"numbers[-1] = {numbers[-1]}")
    print(f"numbers[-2] = {numbers[-2]}")
    print(f"numbers[-3] = {numbers[-3]}")
    print(f"numbers[-4] = {numbers[-4]}")
    print(f"numbers[-5] = {numbers[-5]}")

# function6()

def function7():
    # create a series using list (sequence) with different index positions
    numbers = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
    print(numbers)
    print('-' * 80)

    # positive indexing
    # - never access the values using positions, if the positions do not exist
    # print(f"numbers[0]  = {numbers[0]}")

    # negative indexing
    # - never access the values using positions, if the positions do not exist
    # print(f"numbers[-1] = {numbers[-1]}")
    
    # access values using the given index positions
    print(f"numbers['a']  = {numbers['a']}")
    print(f"numbers['b']  = {numbers['b']}")
    print(f"numbers['c']  = {numbers['c']}")
    print(f"numbers['d']  = {numbers['d']}")
    print(f"numbers['e']  = {numbers['e']}")

# function7()

def function8():
    # create a series using list (sequence)
    numbers = pd.Series([10, 20, 30, 40, 50])
    print(numbers)
    print('-' * 80)

    # arithmetic broadcast operation

    # broadcast addition operation
    print("adding 10 to every member")
    print(numbers + 10)
    print('-' * 80)

    # broadcast mmultiplication operation
    print("multiplying every member by 10")
    print(numbers * 10)
    print('-' * 80)

    # comparison broadcast operations

    # broadcast == operation
    print("numbers == 10")
    print(numbers == 10)
    print('-' * 80)

    # broadcast >= operation
    print("numbers >= 30")
    print(numbers >= 30)
    print('-' * 80)

# function8()

def function9():
    # create a series using list (sequence)
    numbers = pd.Series([10, 20, 30, 10, 40, 50])
    print(numbers)
    print('-' * 80)

    # statistical operations
    print(f"sum of all numbers           = {numbers.sum()}")
    print(f"mean of all numbers          = {numbers.mean()}")
    print(f"median of all numbers        = {numbers.median()}")
    print(f"mode of all numbers          = {numbers.mode()[0]}")
    print(f"minimum of all numbers       = {numbers.min()}")
    print(f"maximum of all numbers       = {numbers.max()}")
    print(f"variance of all numbers      = {numbers.var()}")
    print(f"std. division of all numbers = {numbers.std()}")
    print('-' * 80)

    # get all statistical information 
    print(numbers.describe())

# function9()

def function10():
    # create a series using list (sequence)
    numbers = pd.Series([10, 20, 30, 40, 50])
    print(numbers)
    print('-' * 80)

    # use arithmetic broadcast operation
    # print(numbers ** 3)

    # apply a function on the series object
    print(pd.Series(map(lambda n: n ** 3, numbers)))
    print('-' * 80)

    print(numbers.apply(lambda n: n ** 3))

# function10()

def function11():
    # create a series with string values
    fruits = pd.Series(['apple', 'banana', 'cherry', 'GUAVA', 'PineApple'])
    print(fruits)
    print('-' * 80)

    # perform string operations on series object
    print(f"converting all the values to lower case")
    print(fruits.str.lower())
    print('-' * 80)

    print(f"converting all the values to lower case")
    print(fruits.str.upper())
    print('-' * 80)

    print(f"length of every value in series")
    print(fruits.str.len())
    print('-' * 80)

    print(f"replacing values")
    print(fruits.str.replace('a', 'o'))
    print('-' * 80)

# function11()

def function12():
    # create a series using list (sequence)
    numbers = pd.Series([10, 4, 3, 15, 50])
    print(numbers)
    print('-' * 80)

    # sort the values in ascending order
    print(numbers.sort_values())
    print('-' * 80)

    # sort the values in ascending order
    print(numbers.sort_values(ascending=False))
    print('-' * 80)

# function12()


def function13():
    # create a series using dictionary
    # note: the series is storing values 10, 20, 30, 40 
    #   on the index positions 'a', 'b', 'c' and 'd'
    series = pd.Series({'a': 10, 'b': 20, 'c': 30, 'd': 40})
    print(series)

    print(series + 10)
    print(series == 10)

# function13()

def function14():
    # series object 
    series = pd.Series([10, 20, 30, 40, 50], index=['a', ['b', 'c'], 'd', 'e', 'f'])
    print(series)

    print(f"index = {series.index}")
    # print(f"series['a'] = {series['a']}")
    # print(f"series['b'] = {series['b']}")

# function14()