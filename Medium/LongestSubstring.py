class Solution:
    def lengthOfLongestSubstring(self: str) -> int:
        charSet = set()  # create set to hold current window fo elements
        l = 0  # left edge of sliding window
        res = 0  # length of longest substring

        for r in range(len(self)):
            while self[r] in charSet:
                charSet.remove(self[l])
                l += 1
            charSet.add(self[r])
            res = max(res, r - l + 1)
        return res
