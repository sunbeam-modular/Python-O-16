# statement
# - unit of execution

# block
# - group of statements
# - python uses indentation for creating a block of statement

# control flow keyword: (if .. else)
# - when a condition returns True, if block gets executed
# - when a condition returns False, else block gets executed

# input()
# - used to get input from user
# - returns a string (sequence of characters)
# - all input values given by user, will be always in the string format
# - if required, convert the string data type to the required data type

# get input from user and convert it in int data type
age = int(input("enter your age: "))
country = input("enter your country: ")

# logic: if person's age is >= 18, person will be eligible for voting, otherwise no
if age >= 18:
    # if block (will be executed when the condition is True)
    print("Yes, the person is eligible for voting")
    print("next statement in if block")
else:
    # else block (will be executed when the condition is False)
    print("No, the person is NOT eligible for voting")
    print("next statement in else block")

# this will add a blank line on console
print()

# logic
# - if age is >= 18 and the conutry is "india", then person is eliible, otherwise no

if age >= 18 and country == "india":
    print("person is eligible for voting")
else:
    print("person is NOT eligible for voting")