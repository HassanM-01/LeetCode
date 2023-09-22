from typing import List


def evalRPN(self, tokens: List[str]) -> int:
    stack = []  # create stack
    for c in tokens:  # loop through input
        if c == '+':  # check for operand
            stack.append(stack.pop() + stack.pop())  # pop last two elements and append result
        elif c == '-':
            a, b = stack.pop(), stack.pop()  # assign popped elements to variables in order to switch ordering
            stack.append(b - a)  # append result
        elif c == '*':
            stack.append(stack.pop() * stack.pop())  # pop last two elements and append result
        elif c == '/':
            a, b = stack.pop(), stack.pop()  # assign popped elements to variables in order to switch ordering
            stack.append(int(b / a))  # cast to int to round to integer
        else:
            stack.append(int(c))
        return stack[0]  # return top of stack
