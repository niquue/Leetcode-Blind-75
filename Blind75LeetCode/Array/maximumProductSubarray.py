"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""

def maxProduct(nums):

    if len(nums) == 1:
        return nums[0]
    res = [1] * len(nums)
    res[0] = nums[0]

    for i in range(len(nums)):
        if res[i - 1] < 0:
            res[i] = nums[i]
        else:
            res[i] = res[i - 1] * nums[i]
    return max(res)


result = maxProduct([2, 3, -2, 4])
print(result)