from collections import deque
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Initialize array of potential answers
        rectangle_sizes = []
        fully_used = set()
        # Iterate over heights
        for i, height in enumerate(heights):
            print("current height: " + str(height))
            if i in fully_used:
                print("i skipped index: " + str(i))
                continue
            left_stack = deque(heights[0:i])
            right_stack = deque(heights[-1:i:-1])

            # The consecutive count is the count of how many chaining neighbours are equal to the current height or
            # larger. Starts off as 1, because the current height itself also counts.
            consecutive_count = 1

            # Pop from the left stack, see if it matches up to the current height. If so, increment the consecutive
            # count
            while len(left_stack) > 0:
                popped_value = left_stack.pop()
                if popped_value > height:
                    consecutive_count += 1
                elif popped_value < height:
                    break
                elif popped_value == height:
                    consecutive_count += 1
                    fully_used.add(i - consecutive_count + 1)

            # Pop from the right stack, see if it matches up to the current height. If so, increment the consecutive
            # count
            while len(right_stack) > 0:
                popped_value = right_stack.pop()
                if popped_value > height:
                    consecutive_count += 1
                elif popped_value < height:
                    break
                elif popped_value == height:
                    consecutive_count += 1
                    fully_used.add(i + consecutive_count - 1)

            # Append the rectangle size to the array of potential answers
            rectangle_sizes.append(consecutive_count * height)

        return max(rectangle_sizes)


"""
Explanation:
Iterate over the heights. For each height, make a stack of the heights on its left and a stack of the heights on its 
right. Then, to determine the rectangle that can be formed using this height H, pop from the left stack and see if the 
height is higher or equal to H. If so, add it to the count of consecutive heights. If not, repeat this step for the right
stack. You do not need to increment the consecutive height count if the popped value is lower than the index value,
because the lower value will have its own turn too when it is being iterated over. You just want to find for every
height what the maximum consecutive heights of H you can reach. 

Finally multiply the count of consecutive height H by the value H. Add it to the possible result set. 
Do this for every height in the array. At the end, get the maximum surface area from the possible result set.  
"""
