def characterReplacement(self, s: str, k: int) -> int:
    count = {}  # count occurrence of characters
    res = 0  # length of longest substring/window

    l = 0  # initialize left pointer
    for r in range(len(s)):  # loop over chars in string
        count[s[r]] = 1 + count.get(s[r], 0)  # increment occurrences of each char

        while (r - l + 1) - max(count.values()) > k:  # check to see if total replaced chars are =< k
            count[s[r]] -= 1  # decrement occurrences of char at left pointer
            l += 1  # increment left pointer

        res = max(res, r - l + 1)  # calculate max window/substring size
    return res


def characterReplacements(self, s: str, k: int) -> int:
    count = {}

    l = 0
    maxf = 0  # count frequency of most occurring char
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])  # calculate max frequency

        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

    return (r - l + 1)
