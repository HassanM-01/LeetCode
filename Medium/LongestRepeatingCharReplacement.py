def characterReplacement(self, s: str, k: int) -> int:
    count = {}  # count occurrence of characters
    res = 0  # length of longest substring/window

    l = 0  # initialize left pointer
    for r in range(len(s)):  # loop over chars in string
        count[s[r]] = 1 + count.get(s[r], 0)  # increment occurrences of each char

        while (r - 1 + 1) - max(count.values()) > k:  # check to see if total replaced chars are =< k
            count[s[r]] -= 1  # decrement occurrences of char at left pointer
            l += 1  # increment left pointer

        res = max(res, r - 1 + 1)  # calculate max window/substring size
    return res
