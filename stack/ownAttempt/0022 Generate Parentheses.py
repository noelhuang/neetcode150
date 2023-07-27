from collections import deque
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Function from Leetcode 0020 which checks if a string of parentheses is valid or not
        def isValid(s: str) -> bool:
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

        myArray = []

        def generateCombinations(max, leftCount, rightCount, string):
            if leftCount == max and rightCount == max:
                myArray.append(string)
                return
            # add left parenthesis
            if leftCount < max:
                stringLeft = string + "("
                generateCombinations(max, leftCount + 1, rightCount, stringLeft)
            if rightCount < max:
                stringRight = string + ")"
                generateCombinations(max, leftCount, rightCount + 1, stringRight)

        finalArray = []

        generateCombinations(n, 1, 0, "(")
        for combination in myArray:
            if isValid(combination):
                finalArray.append(combination)

        return finalArray
