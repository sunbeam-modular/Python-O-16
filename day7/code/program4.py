# slicing
# - used to get values from a collection in sequential order of index posititions
# - taking a sequential portion of a collection
# - returns a new list object without having any reference to the existing collection
# - this this result is modified, the existing collection does not get affected
# - if invalid start/stop is provides, slicing returns an empty collection
# - syntax
#   - collection[start:stop:step]
# - start: has default value of 0
# - stop: has default value of len(collection)
# - step: has default value of 1
# step count
# - used to generate the next value
# - when the step count is postive
#   - the values will be retrieved from left to right
#   - the stop value must be greater than start value
# - when the step count is negative
#   - the values will be retrieved from right to left
#   - the start count must be greater the stop value

def function1():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers     = {numbers}")

    # create a new collection with the values from 2nd to 5th position
    new_numbers = []
    for position in range(2, 6):
        # print(f"value at {position} = {numbers[position]}")
        new_numbers.append(numbers[position])        
        # print(f"position = {position}")

    print(f"new numbers = {new_numbers}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers        = {numbers}")

    # create a new collection with the values from 2nd to 5th position
    new_numbers = numbers[2:6:1]
    print(f"numbers[2:6:1] = {new_numbers}")

    # create a new collection with the values from 2nd to 5th position
    # since the step has a default value of 1, it can be skipped
    new_numbers = numbers[2:6]
    print(f"numbers[2:6]   = {new_numbers}")

# function2()

def function3():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers        = {numbers}")

    # mention start, stop and step
    print(f"numbers[0:6:1] = {numbers[0:6:1]}")

    # since the step has default value 1, lets skip it
    print(f"numbers[0:6]   = {numbers[0:6]}")

    # since the start has default value 0, lets skip it
    print(f"numbers[:6]    = {numbers[:6]}")

# function3()

def function4():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers         = {numbers}")

    # mention start, stop and step
    print(f"numbers[6:10:1] = {numbers[6:10:1]}")

    # since the step has default value 1, lets skip it
    print(f"numbers[6:10]   = {numbers[6:10]}")

    # since the stop has default value as len(collection), lets skip it
    print(f"numbers[6:]     = {numbers[6:]}")

# function4()

def function5():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers          = {numbers}")

    # get all the values
    print(f"numbers[0:10:1]  = {numbers[0:10:1]}")

    # skip the step count as it has default value 1
    print(f"numbers[0:10]    = {numbers[0:10]}")

    # skip the stop as it has default value len(collection)
    print(f"numbers[0:]      = {numbers[0:]}")

    # skip the start as it has default value 0
    print(f"numbers[:]       = {numbers[:]}")

    # skip the start as it has default value 0
    print(f"numbers[::]      = {numbers[::]}")

    # skip the start as it has default value 0
    print(f"numbers[::1]      = {numbers[::1]}")

# function5() 

def function6():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers          = {numbers}")

    # start from -6 and go till -1 (from left to right)
    print(f"numbers[-6:-1:1] = {numbers[-6:-1:1]}")

    # start from -6 and go till -1 (from left to right)
    print(f"numbers[-6:-1]   = {numbers[-6:-1]}")

# function6()


def function7():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers           = {numbers}")

    # get the values from 6 to 0 (from right to left)
    print(f"numbers[6:0:-1]   = {numbers[6:0:-1]}")

    # get the values from 6 to 0 (from right to left)
    # since the stop here will reach to the first value, lets skip it 
    print(f"numbers[6::-1]    = {numbers[6::-1]}")

    # since the stop will reach to the 0th position and start will start from the last position, lets skip both of them
    # get all the values in reverse order
    print(f"numbers[::-1]     = {numbers[::-1]}")

    # to get all the values in reverse order, 
    # it always preferred to use ::-1 as it is faster than reversed()
    print(f"reversed(numbers) = {list(reversed(numbers))}")

# function7()

def function8():
    # string data (collection of characters)
    sentence = "I love machine learning"
    print(f"sentence          = {sentence}")
    print('-' * 80)

    # get the required character using +ve index
    print(f"sentence[0]       = {sentence[0]}")
    print(f"sentence[1]       = {sentence[1]}")
    print(f"sentence[2]       = {sentence[2]}")
    print(f"sentence[3]       = {sentence[3]}")
    print('-' * 80)

    # get the required character using -ve index
    print(f"sentenece[-1]     = {sentence[-1]}")
    print(f"sentenece[-2]     = {sentence[-2]}")
    print(f"sentenece[-3]     = {sentence[-3]}")
    print(f"sentenece[-4]     = {sentence[-4]}")
    print(f"sentenece[-5]     = {sentence[-5]}")
    print('-' * 80)

    # slice the word machine from the sentence
    print(f"sentence[7:14]    = {sentence[7:14]}")

    # get the entire sentence in reverse order
    print(f"sentence[::-1]    = {sentence[::-1]}")

function8()