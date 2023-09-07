def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    # Loop over len s since both lengths are the same and use i as the iterator
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)  # check if letter exists in dict then increment
        countT[t[i]] = 1 + countT.get(t[i], 0)  # check if letter exists in dict then increment
    for c in countS:  # loop over keys in dict
        if countS[c] != countT.get(c, 0):  # check if letter exists in both dicts
            return False
    return True


s = "a"
t = "ab"

isAnagram(s, t)
