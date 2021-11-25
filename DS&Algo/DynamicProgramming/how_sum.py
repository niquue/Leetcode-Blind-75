"""
Write a function 'howSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments

The function should return an array containing any combination of elements that add up to exactly
the targetSum. If there is no combination that adds up to the targetSum, then return null.

If there are multiple combinations possible, you may return any single one.]

howSum(7, [5,3,4,7]) -> [3, 4] or [7]
howSum(8, [2,3,5]) -> [2, 2, 2, 2] or [3,5]
howSum(7, [2,4]) -> null
howSum(0, [1,2,3]) -> []

m = target sum
n = numbers.length

Brute Force
------------
time: O(n^m) - we have to consider the cost of: return [*remainder_result, num]
so, O(n^m * m)
space: O(m)

Memoized
-----------
time: O(n*m) array at most m elements long, so O(n*m^2)
space: O(m) - consider space we use in memo object. Keys are unique values of target_sum
Sometimes a value is going to be an array and they will be at most length m
so, O(m*m) = O(m^2)

"""


def how_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers)
        if remainder_result is not None:
            return [*remainder_result, num]
    return None

"""
print(how_sum(7, [2,3])) # [3, 2, 2]
print(how_sum(7, [5,3,4,7])) # [4, 3]
print(how_sum(7, [2,4])) # None
print(how_sum(8, [2,3,5])) # [2, 2, 2, 2]
print(how_sum(300, [7,14])) # None
"""


def memo_how_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = memo_how_sum(remainder, numbers, memo)
        if remainder_result is not None:
            memo[target_sum] = [*remainder_result, num]
            return memo[target_sum]

    memo[target_sum] = None
    return None


print(memo_how_sum(7, [2,3])) # [3, 2, 2]
print(memo_how_sum(7, [5,3,4,7])) # [4, 3]
print(memo_how_sum(7, [2,4])) # None
print(memo_how_sum(8, [2,3,5])) # [2, 2, 2, 2]
print(memo_how_sum(300, [7,14])) # None
