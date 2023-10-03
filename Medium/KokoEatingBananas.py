import math
from typing import List


def minEatingSpeed(self, piles: List[int], h: int) -> int:
    l, r = 1, max(piles)  # initialize left and right pointers
    res = r  # initialize result variable to max num in piles list

    while l <= r:  # loop through range
        k = (l + r) // 2  # initialize mid pointer
        hours = 0  # initialize hours var
        for p in piles:  # loop through piles list
            hours += math.ceil(p / k)  # calculate number of hours to eat bananas
        if hours <= h:  # check if number of hours is less than or equal to the largest possible solution
            res = min(res, k)  # calculate min number of hours and set to res variable
            r = k - 1  # move pointer to the left half to check for smaller solutions
        else:
            l = k + 1  # move pointer to the right half to check for possible solutions
    return res


