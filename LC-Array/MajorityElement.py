from typing import List


def majorityElement(self, nums: List[int]) -> int:
    result, count = 0, 0  # create variables to hold the number of occurrences and the number

    for n in nums:  # iterate over the list
        if count == 0:  # check if the number of occurrences is 0 which means there's no majority element
            result = n  # set current num to result
        count += (1 if n == result else -1)  # increment if the current num is majority or decrement if other num
    return result
