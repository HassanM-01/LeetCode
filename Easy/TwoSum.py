from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    prev = {}  # dict to map index as value and number as key

    for i, n in enumerate(nums):  # loop over list/array
        if target - n in prev:  # check to see if matching number exists as a key in dict
            return [prev[target - n], i]  # return the value of the matching key(index) and the index of the current num
        elif n not in prev:  # check if the number needed to satisfy the requirement does not exist in the dict
            prev[n] = i  # add number as a value and index as key
