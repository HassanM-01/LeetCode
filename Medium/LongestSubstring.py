class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # create set to hold current window fo elements
        l = 0  # left edge of sliding window
        res = 0  # length of longest substring

        for r in range(len(s)):  # loop through string
            while s[r] in charSet:  # check to see if value at right edge of sliding window exists in set
                charSet.remove(s[l])  # remove value at left edge of sliding window
                l += 1  # increment left edge of sliding window
            charSet.add(s[r])  # add value at right pointer
            res = max(res, r - l + 1)  # calculate size of substring
        return res
