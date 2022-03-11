"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""

def containsDuplicate(nums):
    n = set()
    for i in nums:
        if i in n:
            return True
        else:
            n.add(i)
    return False
