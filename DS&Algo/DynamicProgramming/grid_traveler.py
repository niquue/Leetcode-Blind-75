"""
Say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel
to the bottom right corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m * n?

Write a function: gridTraveler(m, n) that calculates this.

gridTraveler(2, 3) = 3
S * *
* * E
1.) right, right, down
2.) right, down, right
3.) down, right, right

O(2^n+m) time
O(n + m) space

"""


# Fairly slow code on using 18x18
def grid_traveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


# print(grid_traveler(1, 1)) # 1
# print(grid_traveler(2, 3)) # 3
# print(grid_traveler(3, 2)) # 3
# print(grid_traveler(3, 3)) # 6
# print(grid_traveler(18, 18)) # 2333606220


# Memoization grid traveler

def new_grid_traveler(m, n, memo=None):
    if memo is None:
        memo = {}
    _key = str(m) + ',' + str(n)

    if _key in memo:
        return memo[_key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[_key] = new_grid_traveler(m - 1, n, memo) + new_grid_traveler(m, n - 1, memo)
    return memo[_key]


print(new_grid_traveler(1, 1)) # 1
print(new_grid_traveler(2, 3)) # 3
print(new_grid_traveler(3, 2)) # 3
print(new_grid_traveler(3, 3)) # 6
print(new_grid_traveler(18, 18)) # 2333606220
print(new_grid_traveler(32, 30))

"""
m * n combinations
Brute force: O(2^n+m) time, O(n+m) time
Memoized: O(m * n) time, O(n + m) space
"""