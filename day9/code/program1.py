# set
# - unordered mutable collection of unique values
# - once created, set can be modified
# - to create set, you can use {} or call set()

# frozenset
# - unordered immutable collection of unique values
# - once created, frozenset can NOT be modified
# - to create frozenset, call frozenset()

def function1():
    # set of values
    s1 = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
    print(f"s1 = {s1}, type = {type(s1)}")

    # add a new value
    s1.add(60)
    print(f"s1 = {s1}, type = {type(s1)}")

# function1()

def function2():
    # immutable set of unique values
    s1 = frozenset([10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50])
    # s1 = frozenset({10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50})
    print(f"s1 = {s1}, type = {type(s1)}")

    # add a new value to the frozenset
    # since frozenset is immutable collection, it can NOT be modified
    # s1.add(60)
    # print(f"s1 = {s1}, type = {type(s1)}")

# function2()

def function3():
    # list of names
    first_names = ['John', 'Emily', 'Michael', 'Sarah', 'William', 'Olivia', 'David', 'Ava', 'James', 'Isabella',
 'Robert', 'Sophia', 'Richard', 'Mia', 'Charles', 'Charlotte', 'Thomas', 'Abigail', 'Donald',
 'Jessica', 'John', 'John', 'Emily', 'John']

    print(f"first_names = {first_names}, length = {len(first_names)}")
    print('-' * 80)

    # find unique names
    unique_first_names = []
    for name in first_names:
        # check if the name is already added to the unique names list
        if name not in unique_first_names:
            # if the name is not added to the list, add it
            unique_first_names.append(name)

    print(f"unique names = {unique_first_names}, length = {len(unique_first_names)}")
    print('-' * 80)

    # find unique names
    unique_first_names = set(first_names)
    print(f"unique names = {unique_first_names}, length = {len(unique_first_names)}")

# function3()
