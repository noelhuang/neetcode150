from collections import deque
from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        myStack = deque()
        for token in tokens:
            if token not in ["-", "+", "*", "/"]:
                myStack.append(int(token))
            else:
                # token was not an integer, so perform arithmetic
                b = myStack.pop()
                a = myStack.pop()
                if token == "/":
                    value = int(a / b)
                elif token == "+":
                    value = a + b
                elif token == "-":
                    value = a - b
                else:
                    value = a * b
                myStack.append(value)
        return myStack.pop()


"""
Use a stack to solve reverse polish notation. 
Iterate over the array of tokens. For each token, if it is a number, add it to the stack. If not, it must be a symbol
for arithmetic operation + - / *. If it is an operator, pop two values from the stack to perform the arithmetic 
operation between those two popped values. Append the value back onto the stack, because it will be used for further 
calculations. 
"""
