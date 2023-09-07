from typing import List


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}  # map the number of occurrences of n to dict
    freq = [[] for i in range(len(nums) + 1)]  # create a list of lists based on size of nums

    for n in nums:  # iterate over nums
        count[n] = 1 + count.get(n, 0)  # count the number of occurrences of n and map key= num value= frequency
    for n, c in count.items():  # loop over key value pairs in count map
        freq[c].append(n)  # append num (n) to index (c) which is count of frequency

    res = []  # create result list
    for i in range(len(freq) - 1, 0, -1):  # iterate over freq list in reverse
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
