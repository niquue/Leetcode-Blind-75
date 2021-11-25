"""
Write a function 'bestSum(targetSum, numbers)' that takes in a targetSum and an array
of numbers as arguments

The function should return an array containing the shortest combination of numbers
that add up to exactly the targetSum.

If there is a tie for the shortest combination, you may return any of the shortest.

bestSum(7, [5,3,4,7]
could be: [3,4], [7]
-> [7]

bestSum(8, [2, 3, 5])
[2,2,2,2]
[2,3,3]
[3,5] <- return

m = target_sum
n = numbers.length
Brute force
Time: O(n^m * m)
Space: O(m^2)

Memoized:
time: O(m^2 * n)
space: O(m^2)

"""


def best_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers)
        if remainder_combination is not None:
            combination = [*remainder_combination, num]
            # if the combination is shorter than the current "shortest", update it
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    return shortest_combination

"""
print(best_sum(7, [5, 3, 4, 7]))  # [7]
print(best_sum(8, [2, 3, 5]))  # [3, 5]
print(best_sum(8, [1, 4, 5]))  # [4, 4]
print(best_sum(100, [1, 2, 5, 25]))  # [1, 2, 5, 25]
"""


def memo_best_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = memo_best_sum(remainder, numbers, memo)
        if remainder_combination is not None:
            combination = [*remainder_combination, num]
            # if the combination is shorter than the current "shortest", update it
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    memo[target_sum] = shortest_combination
    return shortest_combination


print(memo_best_sum(7, [5, 3, 4, 7]))  # [7]
print(memo_best_sum(8, [2, 3, 5]))  # [3, 5]
print(memo_best_sum(8, [1, 4, 5]))  # [4, 4]
print(memo_best_sum(100, [1, 2, 5, 25]))  # [1, 2, 5, 25]