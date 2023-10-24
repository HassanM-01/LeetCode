def backspaceCompare(self, s: str, t: str) -> bool:
    stack1 = []  # initializes an empty list called stack1 & stack2
    stack2 = []

    for i in s:  # iterates over each character i in the first string s
        if i != "#":  # checks if the character i is not a backspace character
            stack1.append(i)  # append if condition is true
        else:
            stack1.pop()  # removes the last character from stack1, effectively simulating the backspace operation

    for y in t:
        if y != "#":
            stack2.append(y)
        else:
            stack2.pop()

    return stack1 == stack2  # compare the two lists and return true or false
