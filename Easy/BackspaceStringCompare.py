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


def backspaceCompare2(self, s: str, t: str) -> str:
    actual = ""
    hash_count = 0
    for char in reversed(s):
        if char == "#":
            hash_count += 1
        if hash_count == 0:
            actual += char
        if hash_count != 0:
            hash_count -= 1
            continue
    return actual