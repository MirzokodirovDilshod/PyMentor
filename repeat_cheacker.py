# PyMentor
# 10.11.2026
# If there is a repeated symbol in given array return True else return False
def repeated(nums):
    if len(nums) != len(set(nums)):
        return True
    else:
        return False
# We use set to check the repeated thing in our array
# Set removes the duplicates so if the length of array is shorter when it's in the set 
# The given array automaticially becomes shorter and we know that the array had repeated object
# The set is capable to remove the duplicated things in array
# But it can't have any order because set always returns objects without any order