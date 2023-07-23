from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        my_deque = deque()
        for i in range(0, len(s)):
            char = s[i]
            if char == "(" or char == "{" or char == "[":
                my_deque.append(char)
            else:
                try:
                    top_of_stack = my_deque.pop()
                except IndexError:
                    return False
                if char == ")" and top_of_stack != "(":
                    return False
                elif char == "]" and top_of_stack != "[":
                    return False
                elif char == "}" and top_of_stack != "{":
                    return False
        if len(my_deque) == 0:
            return True
        else:
            return False
