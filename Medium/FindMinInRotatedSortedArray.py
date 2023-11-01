from typing import List


def findMin(self, nums: List[int]) -> int:
    res = nums[0]  # initialize return value
    l, r = 0, len(nums) - 1  # initialize left and right pointers

    while l <= r:  # loop through list
        if nums[l] < nums[r]:  # check if left pointer is less than right meaning you're in the lowest sorted half
            res = min(res, nums[l])  # calculate result value
            break  # break out of loop since result condition is met

        m = (l + r) // 2  # initialize middle/pivot var
        res = min(res, nums[m])  # calculate result value

        if nums[m] >= nums[l]:  # check to see if left pointer needs to be moved to the other half
            l = m + 1
        else:
            r = m - 1  # check to see if right pointer needs to be moved to the other half

    return res  # return result var

