from collections import deque
from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        myStack = deque()
        value = None
        for i, token in enumerate(tokens):
            try:  # check if token is integer, if so add it onto stack
                myInt = int(token)
                print(myInt)
                myStack.append(myInt)
            except ValueError:
                # token was not an integer, so perform arithmetic
                if value is None:
                    b = myStack.pop()
                    a = myStack.pop()
                else:
                    a = value
                    b = myStack.pop()
                if token == "/":
                    value = math.trunc(a / b)
                    print(f"Perform{a} // {b}, value = {value}")
                elif token == "+":
                    value = a + b
                    print(f"Perform{a} + {b}, value = {value}")
                elif token == "-":
                    value = a - b
                    print(f"Perform{a} - {b}, value = {value}")
                elif token == "*":
                    value = a * b
                    print(f"Perform{a} * {b}, value = {value}")
        return value
