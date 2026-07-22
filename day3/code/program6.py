# special operator (is and is not)
# - used to compare boolean values and None
# - prefere using is or is not over == or !=

can_vote = True

# is operator
print(f"{can_vote} is True      = {can_vote is True}")
print(f"{can_vote} is False     = {can_vote is False}")
print(f"{can_vote} is None      = {can_vote is None}")

print()

# is not operator (answer is always be opposite of is operator)
print(f"{can_vote} is not True  = {can_vote is not True}")
print(f"{can_vote} is not False = {can_vote is not False}")
print(f"{can_vote} is not None  = {can_vote is not None}")
