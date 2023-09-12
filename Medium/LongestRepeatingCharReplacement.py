def characterReplacement(self, s: str, k: int) -> int:
    count = {}
    res = 0

    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - 1 + 1) - max(count.values()) > k:
            count[s[r]] -= 1
            l += 1

        res = max(res, r -1 + 1)
    return res
