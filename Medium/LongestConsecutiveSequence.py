from typing import List


def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums)  # create set from list of nums
    longest = 0  # initialize variable to hold length of longest sequence

    for n in nums:  # loop over list
        if (n - 1) not in numSet:  # check if number is beginning of a sequence
            length = 0  # intialize length variable
            while (n + length) in numSet:  # continue to loop while sequence continues
                length += 1  # increment length variable
            longest = max(length, longest)  # calculate longest substring

    return longest
