from typing import List


def containsDuplicate(self, nums: List[int]) -> bool:
    hashset = set()  # create empty set to hold nums as we iterate

    for n in nums:  # loop over list of nums
        if n in hashset:  # check if num exists in set already
            return True
        hashset.add(n)  # add num to hashset
    return False
