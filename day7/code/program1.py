# list methods
# - sort()
#   - used to sort the values in the list
#   - unlike sorted(), the sort() modifies the existing list
#   - once called on the list, the original order of the list is lost
#   - to avoid loosing the original order, always create a copy of the list before calling the sort()
#   - does not return anything
# - reverse()
#   - used to reverse the values in the list
#   - unlike reversed(), the reverse() modified the existing list
#   - does not return anything
#   - to avoid loosing the original order, always create a copy of the list before calling the reverse()
# - copy()
#   - used to create a shallow copy of a list

# reference creation
# - no new memory will be allocated for the inner values of the collection
# - if one gets modified, other also gets updated

# shallow copy
# - creating new memory for the outer container
# - but, it does not allocate memory for nested objects
# - copy() method is used to create a shallow copy of existing list
# - shallow copy requires lesser memory than deep copy

# deep copy
# - creating new memory for all the nested objects recursively
# - requires more memory 
# - use copy package deepcopy() function

def function1():
    # list of numbers
    numbers = [40, 20, 10, 30, 50]
    print(f"original numbers           = {numbers}")

    # sort the list in ascending order
    # the original collectios gets updated
    numbers.sort()
    print(f"ascending ordered numbers  = {numbers}")

    # sort the list in descending order
    numbers.sort(reverse=True)
    print(f"descending ordered numbers = {numbers}")

# function1()

def function2():
    # list of numbers
    numbers = [40, 20, 10, 30, 50]
    print(f"original numbers           = {numbers}")

    # reverse the list 
    numbers.reverse()
    print(f"reversed numbers           = {numbers}")

function2()

def function3():
    # list of numbers
    numbers = [40, 20, 10, 30, 50]
    print(f"original numbers           = {numbers}")

    # create a shallow copy of the numbers collection
    numbers_clone = numbers.copy()
    print(f"numbers clone              = {numbers_clone}")

    # sort the cloned list
    numbers_clone.sort()
    print(f"sorted numbers clone       = {numbers_clone}")

    # check if the original collection is modified
    print(f"original numbers           = {numbers}")
    
# function3()

def function4():
    # list of numbers
    numbers = [40, 20, 10, 30, 50]
    print(f"original numbers           = {numbers}")
    
    # create a copy by using another variable
    # note: this statement will NOT create a copy of numbers
    #       instead it create another reference to the existing collection
    # which means, if any of the collections gets updated, the other one will also gets affected
    numbers_clone = numbers
    print(f"numbers_clone              = {numbers_clone}")

    # update the numbers_clone
    numbers_clone.append(90)
    print(f"numbers_clone              = {numbers_clone}")    
    print(f"original numbers           = {numbers}")

    # update the original numbers
    numbers.append(70)
    print(f"numbers_clone              = {numbers_clone}")    
    print(f"original numbers           = {numbers}")

# function4()    

