# list comprehension as filter
# - [<tmp var> for <tmp var> in <collection> if <condition>]

def function1():
    # list of numbers
    numbers = [10, 39, 89, 71, 82, 45, 38, 19, 17, 49]
    print(f"numbers      = {numbers}")

    # find all even numbers
    even_numbers = [n for n in numbers if n % 2 == 0]
    print(f"even numbers = {even_numbers}")

    # find all odd numbers
    odd_numbers = [n for n in numbers if n % 2 != 0]
    print(f"odd numbers  = {odd_numbers}")

# function1()

def function2():
    # list of emails
    emails = ['amit@test.com', 'johnexample.com', 'jane@ms.com', 'tim@apple.com']
    print(f"emails         = {emails}")

    # find invalid emails
    invalid_emails = [email for email in emails if '@' not in email]
    print(f"invalid emails = {invalid_emails}")

# function2()

def function3():
    # marks of students
    marks = [20, 10, 40, 25, 11, 9, 49, 38]
    print(f"marks           = {marks}")

    # find the students who failed in the exam
    failed_students = [m for m in marks if m < 15]
    print(f"failed students = {failed_students}")

# function3()

def function4():
    # list of numbers
    numbers = [10, 39, 89, 71, 82, 45, 38, 19, 17, 49]
    print(f"numbers             = {numbers}")

    # get square of even numbers
    even_number_squares = [n ** 2 for n in numbers if n % 2 == 0]
    print(f"even_number_squares = {even_number_squares}")

# function4()

def function5():
    # list of numbers
    numbers = (10, 39, 89, 71, 82, 45, 38, 19, 17, 49)
    print(f"numbers      = {numbers}")

    # find all even numbers using tuple comprehension
    even_numbers = tuple(n for n in numbers if n % 2 == 0)
    print(f"even numbers = {even_numbers}")

# function5()

def function6():
    # list of names
    names = ['john', 'jane', 'alice', 'bob']
    print(f"names     = {names}")

    # dictionary comprehension
    # {0: "john", 1: 'jane', 2: 'alice', 3: 'bob'}
    result = {index:name for index, name in enumerate(names)}
    print(f"result    = {result}")

function6()
