from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        my_deque = deque()
        my_array = [0 for i in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            if len(my_deque) == 0:
                my_deque.append((i, temp))
            else:
                flag = True
                while len(my_deque) > 0 and flag:
                    top_value = my_deque[-1]
                    if temp > top_value[1]:
                        delta_index = i - top_value[0]
                        my_array[top_value[0]] = delta_index
                        my_deque.pop()
                    else:
                        flag = False
                my_deque.append((i, temp))
        return my_array

# TODO: Optimize
"""
Explanation:
Iterate over the temperatures. Initialize stack, which will contain (index, temperature) tuple.
Compare temperature to top value of stack. If none, append to stack including the index. 
If temperature > popped value of stack, calculate delta in index. THe delta index should be added in an array at the 
index of the popped value. 
"""