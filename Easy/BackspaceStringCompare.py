def backspaceCompare(self, s: str, t: str) -> bool:
    stack1 = []
    stack2 = []

    for i in s:
        if i != "#":
            stack1.append(i)
        else:
            stack1.pop()

    for y in t:
        if y != "#":
            stack2.append(y)
        else:
            stack2.pop()

    return stack1 == stack2