arr = [3, 7, 5, 6, 2, 8, 3]


def subsetA(arr):
    res = []
    arr.sort(reverse=True)
    print(arr)
    minimum = len(arr) // 2
    sum = 0
    sum_b = 0

    for i in range(minimum):
        sum += arr[i]
    for y in range(minimum + 1, len(arr) - 1):
        sum_b += arr[y]
    print(sum)
    print(sum_b)
    if sum >= sum_b:
        res = arr[:minimum]
    print(res)
    return res



subsetA(arr)
