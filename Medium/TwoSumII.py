from typing import List


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1  # initialize left and right pointers

    while l < r:    # loop through numbers while left pointer doesn't cross right pointer
        curSum = numbers[l] + numbers[r]    # current sum = value of both l + r pointers

        if curSum > target:     # move right pointer to the left if sum is too large
            r -= 1
        elif curSum < target:   # move left pointer to the right if sum is too low
            l += 1
        else:
            return [l + 1, r + 1]  # return indices of curr sum
