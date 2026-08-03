# string methods
# - converting case
#   - title(): convert first letter of every word to upper case
#   - lower(): convert all letters of string to upper case
#   - upper(): convert all letters of string to lower case
#   - swapcase(): convert upper to lower and vice-a-versa
# - remove the spaces
#   - lstrip(): remove left side spaces
#   - rstrip(): remove right side spaces
#   - strip(): remove spaces from both the sides
# - replace letters with new ones
#   - replace(): used to replace one or more letters with another string
# - find substring
#   - find(): returns the index of substring if it present, -1 otherwise
#   - index(): returns the index of substring if it present, raises error otherwise
# - statrs/ends with
#   - startswith(): returns True if string starts with required pattern
#   - endswith(): return True if string ends with required pattern
# - split and join
#   - split(): returns a list of parts separated by the pattern
#   - join(): used to join multiple parts from a list of strings into a single string

def function1():
    # string
    text = "Python programming"
    print(f"text       = {text}")
    print('-' * 80)

    # change case
    print(f"uppper     = {text.upper()}")
    print(f"lower      = {text.lower()}")
    print(f"swapcase   = {text.swapcase()}")
    print(f"title case = {text.title()}")

# function1()

def function2():
    # string with spaces on both the sides
    text = "  python programming   "
    print(f"text        = {text}")
    print('-' * 80)

    # remove spaces
    print(f"lstri()     = {text.lstrip()}")
    print(f"rstrip()    = {text.rstrip()}")
    print(f"strip()     = {text.strip()}")

# function2()

def function3():
    # string
    text = "hello Java"
    print(f"text                        = {text}")
    print('-' * 80)

    # replace words
    print(f"replacing java with python = {text.replace('Java', 'Python')}")

# function3()

def function4():
    # string
    text = "python programming"
    print(f"text                    = {text}")
    print('-' * 80)

    # find substrings
    print(f"index of 'python'       = {text.find('python')}")
    print(f"index of 'python'       = {text.index('python')}")
    print(f"index of 'programming'  = {text.find('programming')}")

    # since javs word does not exist, find() returns -1
    print(f"index of 'java'         = {text.find('java')}")
    # print(f"index of 'java'         = {text.index('java')}")

# function4()
    
def function5():
    # string
    file_name = "my_file.txt"
    print(f"file_name                       = {file_name}")
    print('-' * 80)

    # check if string starts with a pattern
    print(f"file_name starts with 'my_file' = {file_name.startswith('my_file')}")
    print(f"file_name starts with 'my_doc'  = {file_name.startswith('my_doc')}")

    # check if string ends with a pattern
    print(f"file_name ends with 'txt'       = {file_name.endswith('txt')}")
    print(f"file_name ends with 'docx'      = {file_name.endswith('docx')}")

# function5()

def function6():
    # names
    names = ['amit kulkarni', 'amitabh bachchan', 'amit tripathi', 'mohan joshi', 'amit joshi']

    # find names starting with 'amit'
    for name in names:
        print(f"{name} starts with 'amit' = {name.startswith('amit')}")
    print('-' * 80)

    # find all the names starting with amit
    does_name_match_with_pattern = lambda name: name.startswith('amit')
    print(list(filter(does_name_match_with_pattern, names)))
    print([name for name in names if does_name_match_with_pattern(name)])

# function6()

def function7():
    # string
    fruits = 'apple,banana,orange,pineapple'
    print(f"fruits      = {fruits}")
    print('-' * 80)

    # split all the fruit names in a list
    print(f"fruit names = {fruits.split(',')}")
    print('-' * 80)

    # string url
    url = "https://google.co.in?q=python+programming"
    print(f"url = {url}")
    print('-' * 80)

    # split the url with ://
    scheme, rest_of_url = url.split('://')
    print(f"scheme       = {scheme}, rest_of_url = {rest_of_url}")

    # split rest_of_url with ?
    domain_name, query_sting = rest_of_url.split('?')
    print(f"domain name  = {domain_name}")
    print(f"query string = {query_sting}")

# function7()

def function8():
    # list of fruits
    fruits = ['apple', 'banana', 'orange', 'pineapple']
    print(f"fruits           = {fruits}")
    print(f"string from list = {' '.join(fruits)}")
    print(f"string from list = {'-'.join(fruits)}")
    print(f"string from list = {'*'.join(fruits)}")
    print('-' * 80)

    names = ['john', 'jane', 'david', 'alice', 'bob']
    print(f"names            = {names}")
    print(f"join all names   = {','.join(names)}")
    print(f"join all names   = {'-'.join(names)}")

# function8()

