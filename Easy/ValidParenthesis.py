def isValid(self, s: str) -> bool:
    stack = []  # create stack to hold opening brackets
    paren_check = {")": "(", "]": "[", "}": "{"}  # create dict of paren with closing paren as key and opening as value

    for i in s:  # loop over string
        if i in paren_check:    # check if I is a closing paren
            if stack and stack[-1] == paren_check[i]:   # check if stack is not empty and that the value in dict is the correct opening paren
                stack.pop()     # remove the paren from the stack
            else:
                return False    # return False if paren does not match
        else:
            stack.append(i)     # append if i is an opening paren
    return True if not stack else False     # return true if stack is empty
