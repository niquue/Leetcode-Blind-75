"""
Write a function 'canSum(targetSum, numbers)' that takes in a targetsum and an array of numbers as arguments.

The function should return a boolean indicating whether or not it is possible to generate the targetsum using numbers
from the array.

You may use an element of the array as many times as needed,
You may assume that all input numbers are nonnegative.

canSum(7, [5,3,4,7]) -> True, ie 3+4
canSum(7, [2,4]) -> False

Brute Force
------------
Complexity of O(n^m) time
O(m) space

Memoized
----------
O(m*n) time
O(m) space
"""

# Not an optimized function slows on large input of target_sum
def can_sum(target_sum, numbers):
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for i in numbers:
        remainder = target_sum - i
        if can_sum(remainder, numbers):
            return True
    return False

"""
print(can_sum(7, [2,3])) # True
print(can_sum(7, [5,3,4,7])) # True
print(can_sum(7, [2,4])) # False
print(can_sum(8, [2,3,5])) # True
print(can_sum(300, [7,14])) # False
"""


def memo_can_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for i in range(len(numbers)):
        remainder = target_sum - numbers[i]
        if memo_can_sum(remainder, numbers, memo):
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False


print(memo_can_sum(7, [2,3]))  # True
print(memo_can_sum(7, [5,3,4,7]))  # True
print(memo_can_sum(7, [2,4]))  # False
print(memo_can_sum(8, [2,3,5]))  # True
print(memo_can_sum(300, [7,14]))  # False

