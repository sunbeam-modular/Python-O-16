# Exception handling

def function1():
    n1 = int(input("enter n1: "))
    n2 = int(input("enter n2: "))

    try:
        print("try block called")
        # application my raise an error 
        answer = n1 / n2

    # handle any exception
    except Exception:
        # gets executed only when there is an exception
        print("except block called")
        print("exception handled")

    else:
        # gets executed only when there is no exception raised
        print("else block called")
        print(f"answer = {answer}")

    finally:
        # gets executed when there is an exception or there is no exception
        print("finally block called")

# function1() 

def function2():
    try:
        n1 = int(input("enter n1: "))
        n2 = int(input("enter n2: "))
        answer = n1 / n2

        # since file named myfile.txt does not exist
        # this statement will raise an exception: FileNotFoundException
        file = open("myfile.txt", "r")
        print(file.read())

        # nested try block
        try:
            print("nother try")
        except:
            print("except block of nested try block")

    except ZeroDivisionError:
        print(f"n2 can not be zero")

        # nested try block
        try:
            print("nother try")
        except:
            print("except block of nested try block")
    except ValueError:
        print(f"you have entered a wrong value")
    except Exception:
        print("Exception: exception handled")
    # except:
    #     print("Generic: exception handled")
    else:
        print(f"answer = {answer}")
    finally:
        print("finally block called")

# function2()


# custom exception class
class InvalidAgeException(Exception):
    def __init__(self):
        super().__init__("invalid age detected")

def function3():
    try:
        age = int(input("enter age: "))
        print(f"age = {age}")

        if age < 0 or age > 80:
            # raise an exception for caller to identify invalid age
            # raise Exception("invalid age detected")
            raise InvalidAgeException()
        
    except ValueError:
        print("enter number value")
    # except:
    #     print("Generic except block")

function3()