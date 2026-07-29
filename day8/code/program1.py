# tuple
# - immutable ordered collection of similar or dissimilar values
# - both indexing and slicing features can be applied on tuple as well
# - packing
#   - adding the values in a tuple
#   - when () are not used, python by default packs the values a tuple
# - unpacking
#   - unpack the values from the collection (tuple/list) into different variables 
#   - assigns value(s) from collection (tuple/list) into multiple variables

# to ignore a value use underscore (_) as variable name
# python allows _ to be declared a variable which is not used anywhere in the code
# _ is used to avoid the warning "unused variable"

def function1():
    # tuple packing: cerate a tuple by adding these values together
    numbers = 10, 20, 30, 40, 50
    print(f"numbers = {numbers}, type = {type(numbers)}")

# function1()

def function2():
    # tuple of numbers
    numbers = 10, 20, 30
    print(f"numbers      = {numbers}, type = {type(numbers)}")
    print('-' * 80)

    # print the values individually
    print(f"first value  = {numbers[0]}")
    print(f"second value = {numbers[1]}")
    print(f"third value  = {numbers[2]}")
    print('-' * 80)

    # store the values in different variables
    n1 = numbers[0]
    n2 = numbers[1]
    n3 = numbers[2]
    print(f"first value  = {n1}")
    print(f"second value = {n2}")
    print(f"third value  = {n3}")

    # perform operation on these variables
    total = n1 + n2 + n3
    print(f"total = {total}")

# function2() 

def function3():
    # tuple of numbers
    numbers = 10, 20, 30
    print(f"numbers      = {numbers}, type = {type(numbers)}")
    print('-' * 80)

    # tuple unpacking
    # - unpack values from numbers tuple into n1, n2, n3 variables
    # - n1 = numbers[0], n2 = numbers[1], n3 = numbers[2]
    n1, n2, n3 = numbers
    print(f"n1 = {n1}, n2 = {n2}, n3 = {n3}")

    # pack the variables into a new tuple
    new_tuple = n1, n2, n3
    print(f"new_tuple = {new_tuple}, type = {type(new_tuple)}")

    # pack the variables into a new tuple with different order
    new_tuple2 = n2, n3, n1
    print(f"new_tuple2 = {new_tuple2}, type = {type(new_tuple2)}")

# function3()

def function4():
    # pack values in a tuple and unpack them into multiple variables
    # - step1: behind the scene, python creates a tuple with 10, 20, 30 and 40 values
    # - step2: python unpacks the tuple into n1, n2, n3 and n4 variables
    n1, n2, n3, n4 = 10, 20, 30, 40
    print(f"n1 = {n1}, n2 = {n2}, n3 = {n3}, n4 = {n4}")

    # pack and unpack 
    p1, p2 = 10, 20
    print(f"p1 = {p1}, p2 = {p2}")

    # swap the values of p1 and p2
    # - p1 should have value of p2
    # - p2 should have value of p1

    # general swapping logic
    # temp = p1
    # p1 = p2
    # p2 = temp
    # print(f"p1 = {p1}, p2 = {p2}")

    # swapping logic implemented in python
    # - step1: creates a new tuple with p2 and p1 = (20, 10)
    # - step2: the newly created tuples gets unpacked into p1 and p2
    p1, p2 = p2, p1
    print(f"p1 = {p1}, p2 = {p2}")

# function4()

def function5():
    # list of numbers
    numbers = [10, 20, 30]
    print(f"numbers = {numbers}, type = {type(numbers)}")

    # unpack the numbers list into variables
    n1, n2, n3 = numbers
    print(f"n1 = {n1}, n2 = {n2}, n3 = {n3}")

# function5()

def function6():
    # variables
    # n1, n2, n3 = 10, 20, 30
    n1 = 10
    n2 = 20
    n3 = 30

    # pack these simple variables into a tuple
    new_tuple = n1, n2, n3
    print(f"new_tuple = {new_tuple}, type = {type(new_tuple)}")

# function6()

def function7():
    # packing and unpacking values
    n1, n2, n3 = 10, 20, 30
    print(f"n1 = {n1}, n2 = {n2}, n3 = {n3}")

    # packing and unpacking with different number of values and variables
    # - by default, the unpacking requires same number of variables as that of number of values
    # - the following statement will raise and error (ValueError)
    # p1, p2 = 10, 20, 30
    # print(f"p1 = {p1}, p2 = {p2}")

    # we need only first and second value from the list of values
    # rest of the values are not required
    # the rest of values (*) will be received in a list collection
    # p1 = 10, p2 = 20 and p3 will receive rest of values (p3 = [30, 40, 50])
    p1, p2, *p3 = 10, 20, 30, 40, 50
    print(f"p1 = {p1}, p2 = {p2}, p3 = {p3}")

    # p1 = [10, 20, 30], p2 = 40, p3 = 50
    *p1, p2, p3 = 10, 20, 30, 40, 50
    print(f"p1 = {p1}, p2 = {p2}, p3 = {p3}")

    # p1 = 10, p2 = [20, 30, 40], p3 = 50
    p1, *p2, p3 = 10, 20, 30, 40, 50
    print(f"p1 = {p1}, p2 = {p2}, p3 = {p3}")

    # python would not allow more than 1 rest-of operator in a given tuple unpacking
    # *p1, *p2, p3 = 10, 20, 30, 40, 50

# function7()

def function8():
    # create a tuple 
    numbers = 10, 20, 30
    print(f"numbers = {numbers}")

    # requirement: need only first and last value and ignore the value 20
    n1, _, n3 = numbers
    print(f"n1 = {n1}, n3 = {n3}")

    # receive only first and third values and ignore rest of the values
    n1, _, n3, _, _ = 10, 20, 30, 40, 50
    print(f"n1 = {n1}, n3 = {n3}")

    # print hello world 5 times
    # since the temp variable is not used anywhere, we can ignore it using _
    for _ in range(5):
        print(f"hello world")

# function8()

def function9():
    # create a tuple 
    numbers = 10, 20, 30, 40, 50

    # unpack tuple and receive only first and last value
    # and ignore rest of the values
    n1, *_, n3 = numbers
    print(f"n1 = {n1}, n3 = {n3}")

# function9()

def function10():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}, type = {type(numbers)}")

    # iterate over the list 
    # drawback of for..in loop: there is no way to access the index positions of the values
    # for value in numbers:
    #     print(f"value = {value}")

    # iterate over the list with index and value
    # enumerate():
    # - returns a collection of tuples
    # for item in enumerate(numbers):
        # print(f"item = {item}")

        # the tuple returned by enumerate function has index on 0th position and value on 1st position
        # print(f"index = {item[0]}, value = {item[1]}")

        # unpack the item tuple into index and value variables
        # index, value = item
        # print(f"index = {index}, value = {value}")
    
    # unpack every item into index and value variables
    for index, value in enumerate(numbers):
        print(f"index = {index}, value = {value}")

function10() 
