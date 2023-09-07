from typing import List


def sortedSquares(self, nums: List[int]) -> List[int]:

    new = []    # create new list

    for n in nums:  # loop through nums
        new.append(n * n)   # square each num and append to new list
    return sorted(new)  # return new list using sorted func
