from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums)  # Create a list 'res' of the same length as the input 'nums'.

    prefix = 1
    for i in range(len(nums)):  # Loop through the 'nums' list from left to right.
        res[i] = prefix  # Set the current element of 'res' to the 'prefix' value.
        prefix *= nums[i]  # Update the 'prefix' by multiplying it with the current element of 'nums'.
    postfix = 1
    for i in range(len(nums) -1, -1, -1):  # Loop through the 'nums' list from right to left.
        res[i] *= postfix   # Update the current element in 'res' by multiplying it with 'postfix'.
        postfix *= nums[i]  # Update 'postfix' by multiplying it with the current element of 'nums'.
    return res
