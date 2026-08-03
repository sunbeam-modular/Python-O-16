# string
# - collection (sequence) of characters
# - one of the built in data types of python
# - built in function
#   - len(): used to get the length of a string
#   - reversed(): used to reverse a string

def function1():
    # declare a variable of type string
    first_name = "john"
    print(f"first_name  = {first_name}, type = {type(first_name)}")

    # declare a variable of type string
    last_name = 'Doe'
    print(f"last_name   = {last_name}, type = {type(last_name)}")

    # declare a string with multiple lines
    article = """
    US President Donald Trump announced he was cancelling a planned attack on Iran with the ‘perimeters of a deal’ agreed to. 
    But his shifting rhetoric is fuelling uncertainty and frustration in Iran, as Al Jazeera’s Tohid Asadi reports from Tehran.
    Published On 2 Aug 2026
    """
    print(f"article = {article}")

# function1()

def function2():
    # string
    name = "john doe"

    # getting length of string
    print(f"length of string = {len(name)}")
    
# function2()

def function3():
    # string
    text = "python programming"

    # positive indexing
    print(f"text[0]  = {text[0]}")
    print(f"text[1]  = {text[1]}")
    print(f"text[2]  = {text[2]}")
    print('-' * 80)

    # negative indexing
    print(f"text[-1] = {text[-1]}")
    print(f"text[-2] = {text[-2]}")
    print(f"text[-3] = {text[-3]}")

# function3()

def function4():
    # string
    text = "python programming"

    # sciling
    print(f"text[0:6]     = {text[0:6]}")
    print(f"text[:6]      = {text[:6]}")
    print(f"text[7:18]    = {text[7:18]}")
    print(f"text[7:]      = {text[7:]}")

    # getting every alternate character
    print(f"text[::2]     = {text[::2]}")

    # reverse a string
    print(f"reversed text = {text[::-1]}")
    print(f"reversed text = {list(reversed(text))}")
    
# function4()

def function5():
    # strings
    str1 = "hello"
    str2 = "python"

    # string concatenation
    print(f"str1 + str2       = {str1 + str2}")
    print(f"str1 + ' ' + str2 = {str1 + ' ' + str2}")

    # string repeatition
    print(f"- * -" * 5)
    print(f"hello " * 5)

# function5()

def function6():
    # string 
    text = "python programming"

    # check membership
    print(f"python in text  = {'python' in text}")
    print(f"java in text    = {'java' in text}")

# function6()
