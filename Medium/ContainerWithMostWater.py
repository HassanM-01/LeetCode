from typing import List


def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1  # initialize l & r pointers
    res = 0  # initialize result var

    while l < r:  # loop through list
        res = max(res, min(height[l], height[r]) * (r - l))  # calculate if current container is more than result
        if height[l] < height[r]:  # move left pointer right if it's less than height[r]
            l += 1
        elif height[r] <= height[l]:  # move right pointer left if it's less than height[l]
            r -= 1

    return res