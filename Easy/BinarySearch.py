from typing import List


def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1  # initialize pointers to beginning and end of list

    while l <= r:   # loop through input list
        m = (l + r) // 2  # calculate mid pointer...(l + r) // 2 can lead to overflow in case of large input
        if nums[m] > target:    # check if mid-pointer is greater than target
            r = m - 1       # move right pointer to left half of mid-pointer
        elif nums[m] < target:  # check if mid-pointer is less than target
            l = m + 1       # move left pointer to right half of mid-pointer
        else:
            return m    # return mid pointer
    return -1
