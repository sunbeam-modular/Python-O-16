# file operations
# - python allows developer to manage the files using file operation functions
# - built-in functions
#   - open(): used to open a file
#     - param1: file path
#     - mode + file type
#     - mode: mode of opening the file
#       - r: 
#         - open the file for reading the contents
#         - if the file does not exist, the code raises an error (FileNotFoundError)
#       - w: 
#         - open the file for writing
#         - if the file does not exist, python will create an empty file first
#         - if the file exists, the new contents will overwrite the existing ones
#       - a:
#         - open the file to appends the contens
#         - if the file already contains some contents, preserve them and add new contents at the end of the file
#       - r+: open file for both read and write
#       - w+: open file for both read and write
# - methods:
#   - read(): 
#     - used to read the contents of the file
#     - by default it reads all the contents of the file
#     - not recommended to read the whole contents if the file has huge contents
#   - read(n):
#     - read only n bytes/characters from the file using the current file read pointer
#   - readlines():
#     - read the contents of a file line by line 
#     - returns list of strings
#   - tell()
#     - the current position file read pointer is pointing
#   - seek():
#     - used to update the file read pointer
#   - close(): used to close the opened file. it is mandatory to close the file after modification.

def function1():
    # open a file for performing a read operation
    file = open("my_file.txt", "r")

    # read all the contents of the file character by charcter
    print(f"contents = {file.read()}")

    # close the file
    file.close()

# function1()

def function2():
    # open a file for performing a read operation
    file = open("my_file.txt", "r")

    # read first 10 characters/bytes from the file
    print(f"contents = {file.read(10)}")

    # read next 10 characters/bytes from the file
    print(f"contents = {file.read(10)}")

    # read next 10 characters/bytes from the file
    print(f"contents = {file.read(10)}")

    # read next 10 characters/bytes from the file
    print(f"contents = {file.read(10)}")

    # close the file
    file.close()

# function2() 

def function3():
    # open a file for performing a read operation
    file = open("my_file.txt", "r")
    print(f"file pointer location = {file.tell()}")

    # read first 10 characters/bytes from the file
    print(f"contents = {file.read(10)}")
    print(f"file pointer location = {file.tell()}")

    # read next 10 characters/bytes from the file
    print(f"contents = {file.read(10)}")
    print(f"file pointer location = {file.tell()}")

    # read next 10 characters/bytes from the file
    print(f"contents = {file.read(10)}")
    print(f"file pointer location = {file.tell()}")

    # read next 10 characters/bytes from the file
    print(f"contents = {file.read(10)}")
    print(f"file pointer location = {file.tell()}")

    # close the file
    file.close()

# function3()

def function4():
    # open a file for performing a read operation
    file = open("my_file.txt", "r")
    print(f"file pointer location = {file.tell()}")

    # by default the file read pointer is pointing at the 0th position
    # change the file read pointer to 5th position 
    file.seek(5)

    print(f"file pointer location = {file.tell()}")
    print(f"contents              = {file.read(10)}")

    # note: since there is not seek() called, the next 10 characters will be read
    print(f"file pointer location = {file.tell()}")
    print(f"contents              = {file.read(10)}")

    # close the file
    file.close()

# function4()

def function5():
    # open a file to write the contents
    file = open("my_file.txt", "w")

    # write some contents
    file.write("India is my country.")

    # close the file
    file.close()

# function5()

def function6():
    # open a file to write the contents
    file = open("my_file.txt", "a")

    # write some contents
    file.write("All indians are by brothers and sisters.")

    # close the file
    file.close()

# function6()

def function7():
    # get input from user
    name = input("enter your name: ")
    address = input("enter your address: ")
    phone = input("enter your phone: ")
    email = input("enter your email: ")

    # open a file to persist the data 
    file = open("person.txt", "w")

    # persist the information
    file.write(f"name: {name}\n")
    file.write(f"address: {address}\n")
    file.write(f"phone number: {phone}\n")
    file.write(f"email: {email}")

    # close the file
    file.close()

# function7()

def function8():
    # read the person information from the file
    file = open("person.txt", "r")

    # read the contents from the file
    # info = file.read()
    # print(info)

    # read the contents from the file in list of strings
    lines = file.readlines()
    # print(f"lines = {lines}")

    # create a person dictionary to store person attributes
    person = {}

    for line in lines:
        # replace the end of the line character with empty string
        line = line.replace('\n', '')
        print(f"line = {line}")

        # separate the attribute and value
        attribute, value = line.split(':')
        print(f"attribute = {attribute}, value = {value}")

        # collect all the attributes in a dictionary
        person[attribute] = value

    # close the file
    file.close()

    print('-' * 80)
    
    # print the person information
    print(person)

function8()