from typing import List


def reverseString(self, s: List[str]) -> None:

    l = 0  # initialize left pointer to beginning of string
    r = len(s) - 1  # initialize right pointer to end of string
    while l < r:  # loop through string
        s[l], s[r] = s[r], s[l]  # switch char at left pointer to char at right pointer & vice versa
        l += 1  # increment left pointer to move towards end of string
        r -= 1  # decrement right pointer to move towards beginning of string
