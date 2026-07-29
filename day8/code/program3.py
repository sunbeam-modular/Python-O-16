# set
# - mutable unordered collection of unique values
# - use {} with values to create a set
# - methods
#   - add(): used to add a new value in the set
#   - remove(): used to remove existing value
#   - union(): adding all the elements of both the sets together (keeping common elements only once)
#   - interesection(): get only the common elements from both the sets
#   - difference(): find the non-common elements from the set
#   - issubset(): check if all values of first set are present in the second set
#   - issuperset(): check if the first set has all the elements from second set
#   - isdisjoint(): check if all values of first set are different than second set

def function1():
    # list of numbers
    numbers_list = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
    print(f"numbers_list  = {numbers_list}, type = {type(numbers_list)}")

    # tuple of numbers
    numbers_tuple = 10, 20, 30, 40, 50, 10, 20, 30, 40, 50
    print(f"numbers_tuple = {numbers_tuple}, type = {type(numbers_tuple)}")

    # set of numbers
    numbers_set = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
    print(f"numbers_set   = {numbers_set}, type = {type(numbers_set)}")

    # set with dissmilar values
    set_with_mixed_values = {True, 10, 20, 50.60, "test"}
    print(f"set_with_mixed_values = {set_with_mixed_values}")

    # set with string values
    fruits = {"apple", "banana", "apple", "guava", "pineapple", "apple"}
    print(f"fruits = {fruits}, type = {type(fruits)}")

# function1()

def function2():
    # set of numbers
    numbers = {10, 20, 30, 40, 50}    
    print(f"numbers   = {numbers}")

    # add a new value
    numbers.add(60)
    numbers.add(60)
    numbers.add(60)
    numbers.add(60)
    numbers.add(60)
    numbers.add(70)
    print(f"numbers   = {numbers}")

    # remove existing value
    numbers.remove(40)
    print(f"numbers   = {numbers}")

    # remove non-existing value
    # - code will raise an error: KeyError
    # numbers.remove(100)
    # print(f"numbers   = {numbers}")

# function2()  

def function3():
    # set of values
    s1 = {10, 20, 30, 40, 50}
    s2 = {40, 50, 60, 70, 80}

    # union of two sets
    print(f"s1.uion(s2) = {s1.union(s2)}")
    print(f"s2.uion(s1) = {s2.union(s1)}")

# function3()

def function4():
    # set of values
    s1 = {10, 20, 30, 40, 50}
    s2 = {40, 50, 60, 70, 80}

    # intersection of two sets
    print(f"s1.intersection(s2) = {s1.intersection(s2)}")
    print(f"s2.intersection(s1) = {s2.intersection(s1)}")

# function4()

def function5():
    # set of values
    s1 = {10, 20, 30, 40, 50}
    s2 = {40, 50, 60, 70, 80}

    # subtracting s1 from s2
    print(f"s1 - s2 = {s1 - s2}")
    print(f"s2 - s1 = {s2 - s1}")

# function5()

def function6():
    # set of values
    s1 = {10, 20, 30, 40, 50, 60, 70, 80}
    s2 = {20, 50, 60}
    s3 = {90, 100}

    # check if s2 is subset of s1
    print(f"s2 subset of s1      = {s2.issubset(s1)}")

    # check if s3 is subset of s1
    print(f"s3 subset of s1      = {s3.issubset(s1)}")

    # check if s1 is superset of s2
    print(f"s1 is superset of s2 = {s1.issuperset(s2)}")

    # check if s1 is superset of s3
    print(f"s1 is superset of s3 = {s1.issuperset(s3)}")

    # check if s1 and s2 are disjoint
    print(f"s1 disjoint s2       = {s1.isdisjoint(s2)}")

    # check if s1 and s3 are disjoint
    print(f"s1 disjoint s3       = {s1.isdisjoint(s3)}")

function6()