"""
Write a function 'fib(n) that takes in a number as an argument.
The function should return the n-th number of the Fibonacci sequence.

The 1st and 2nd number of the sequence is 1.
To generate the next number of the sequence, we sum the previous two.

n:      1, 2, 3, 4, 5, 6, 7, 8, 9, ....
fib(n): 1, 1, 2, 3, 5, 8, 13, 21, 34, .....

If asked for 7, return 13.
fib(7) -> 13

O(2^n) time
O(n) space

fib(50) ~= 2^50 steps = 1.12e+15 = 1,125,899,906,842,624
"""

# This is a sort of naive approach and will take very long to do
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# print(fib(6))
# print(fib(7))
# print(fib(8))
# print(fib(50))


# Memoization
# Use dict, keys will be arg to fn, value will be the return value.
# Fib memoized complexity - O(n) time, O(n) space
mem = dict()


def n_fib(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = n_fib(n - 1, memo) + n_fib(n - 2, memo)
    return memo[n]


print(n_fib(6, mem))
print(n_fib(7, mem))
print(n_fib(8, mem))
print(n_fib(50, mem))

