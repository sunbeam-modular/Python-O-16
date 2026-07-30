# menu driven application

def add(p1: int, p2: int):
    result = p1 + p2
    print(f"addition = {result}")

def subtract(p1: int, p2: int):
    result = p1 - p2
    print(f"subtraction = {result}")

def divide(p1: int, p2: int):
    result = p1 / p2
    print(f"division = {result}")

def multiply(p1: int, p2: int):
    result = p1 * p2
    print(f"multiplication = {result}")

# infinite loop: the loop which never stops
while True:
    # show menu to the user
    print(f"your options are:")
    print(f"1. addition")
    print(f"2. subtraction")
    print(f"3. division")
    print(f"4. multiplication")
    print(f"5. exit")

    # get input from user
    option = int(input("enter your choice: "))

    # get the inputs from user
    n1, n2 = 10, 20

    # perform the requested operation
    if option == 1:
        add(n1, n2)
    elif option == 2:
        subtract(n1, n2)
    elif option == 3:
        divide(n1, n2)
    elif option == 4:
        multiply(n1, n2)
    elif option == 5:
        # stop the loop
        break
    else:
        print("invalid choice, please try again")

    print('-' * 80)
