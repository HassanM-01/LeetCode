from typing import List


def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)  # initialize array to same size as temp array
    stack = []  # create stack [temp, index]

    for i, t in enumerate(temperatures):  # loop over index + temp from temp array
        while stack and t > stack[-1][0]:  # check if stack is not empty and stack temp is less than t
            stackT, stackInd = stack.pop()  # hold temp and index from popped element
            res[stackInd] = i - stackInd  # calculate # of days from indexes and add to result array
        stack.append((t, i))  # add temp + index to stack
    return res
