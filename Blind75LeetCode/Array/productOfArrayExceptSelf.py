"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""

def productExceptSelf(nums):
    copy_nums = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        copy_nums[i] = prefix
        prefix *= nums[i]
    print(copy_nums)
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        copy_nums[i] *= postfix
        postfix *= nums[i]
    return copy_nums

result = productExceptSelf([1,2,3,4])
print(result)