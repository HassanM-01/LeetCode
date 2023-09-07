from typing import List


def moveZeroes(nums: List[int]) -> None:
    l = 0   # make variable for left pointer
    for r in range(len(nums)):  # loop over index of list elements
        if nums[r] != 0:    # check if right pointer is on a non-zero element
            nums[l], nums[r] = nums[r], nums[l] # swap left and right elements
            l += 1  # increment left pointer
    return nums


nums = [2, 2, 0, 1, 4, 12]

moveZeroes(nums)
