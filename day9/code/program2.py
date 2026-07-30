# dictionary
# - mutable collection of key-value pairs
# - every value in dictionary must be associated with a key
# - to create dictionary, use {} or dict()
# - dict() is mostly used to create an empty dictionary
# - key can be of any type (except the collection) but string is preferred
# - key is case sensitive, Address and address are two different keys
# - value can be of any type including collection
# - key must be unique 
# - if same key is used multiple times, it would overwrite the existing value
# - note: 
#   - if {} are used with only values, python would create a set
#   - if {} are used with key-value pairs, python would create a dictionary
#   - empty {} would create empty dictionary and not the empty set
# operations
# - ['<key>']: 
#   - used to get value of key
#   - if the key does not exist, the code raises an error KeyError
#   - use this scheme, when you are sure about the key's existance
# - get():
#   - used to get value of specified key
#   - if the key does not exist, get() returns None (no error raised)
#   - can also return a default value, if the key does not exist in the dictionary
#   - use this scheme, when you are NOT sure about the key's existance
# - keys(): returns list of all keys
# - values(): return list of all values
# - items(): returns list of tuples containing both key and value
# - pop(): used to remove a key along with its value
# - clear(): used to remove all key-value pairs to make the dictionary empty
 
def function1():
    # create an empty dictionary
    empty_dictionary = {}
    print(f"empty_dictionary = {empty_dictionary}, type = {type(empty_dictionary)}")

    # empty set
    empty_set = set()
    print(f"empty_set        = {empty_set}, type = {type(empty_set)}")

    # empty frozenset
    # - this set is useless as once created, it can NOT be modified
    empty_frozen_set = frozenset([])
    print(f"empty_frozen_set = {empty_frozen_set}, type = {type(empty_frozen_set)}")

# function1()

def function2():
    # dictionary of key-value pairs
    person = {
        "first_name": "john",
        "last_name": "doe",
        "age": 40,

        # not recommended to have same key multiple times
        # but if used, the old value would get overwritten
        "age": 50,
        "salary": 50.60,
        "languages": ['english', 'french', 'german']
    }

    print(f"person = {person}, type = {type(person)}")
    print('-' * 80)

    # read values from the dictionary
    print(f"first name  = {person['first_name']}")
    print(f"last name   = {person['last_name']}")
    print(f"age         = {person['age']}")
    print(f"salary      = {person['salary']}")
    print(f"languages   = {person['languages']}")
    print('-' * 80)

    # the line below will raise KeyError as the key address does not exist in person dictionary
    # print(f"address     = {person['address']}")

    # read values from the dictionary
    print(f"first name  = {person.get('first_name')}")
    print(f"last name   = {person.get('last_name')}")
    print(f"age         = {person.get('age')}")
    print(f"salary      = {person.get('salary')}")
    print(f"languages   = {person.get('languages')}")

    # the line below would NOT raise any error, instead it will return None
    print(f"address     = {person.get('address')}")
    print(f"address     = {person.get('address', '-NA-')}")
    print('-' * 80)

    # get list of all keys
    print(f"keys        = {person.keys()}")

    # get list of all values
    print(f"values      = {person.values()}")

# function2()

def function3():
    # dictionary of key-value pairs
    person = {
        "first_name": "john",
        "last_name": "doe",
        "age": 40,
        "salary": 50.60,
        "languages": ['english', 'french', 'german'],
        "address": "USA"
    }

    # iterate over the dictionary
    for key in person:
        print(f"key = {key}, value = {person[key]}")
    print('-' * 80)

    # iterate over the dictionary
    # print(f"items = {person.items()}")
    for key, value in person.items():
        print(f"key = {key}, value = {value}")

# function3()

def function4():
    # dictionary of key-value pairs
    person = {
        "first_name": "john",
        "last_name": "doe"
    }
    print(f"person = {person}")

    # add a new key-value pair
    # - if the key does not exist,  dictionary would create a new item with key and its value
    person['address'] = 'USA'
    print(f"person         = {person}")

    # - if the key exists in the dictionary, the value gets updated
    person['address'] = 'UK'
    print(f"person         = {person}")

    # add a list of languages
    person['languages'] = ['english', 'french']
    print(f"person         = {person}")
    print(f"languages      = {person['languages']}")
    print(f"first language = {person['languages'][0]}")

# function4() 

def function5():
    # dictionary of key-value pairs
    person = {
        "first_name": "john",
        "last_name": "doe",
        "age": 40,
        "salary": 50.60,
        "languages": ['english', 'french', 'german'],
        "address": "USA"
    }
    print(f"person = {person}")
    print('-' * 80)

    # remove address key from person
    # note: if del is used to delete key, it also deletes the value associated with the key
    del person['address']
    print(f"person = {person}")
    print('-' * 80)

    # remove languages key from person
    person.pop('languages')
    print(f"person = {person}")
    print('-' * 80)

    # remove all key-value pairs from person
    person.clear()
    print(f"person = {person}")
    print('-' * 80)

function5()