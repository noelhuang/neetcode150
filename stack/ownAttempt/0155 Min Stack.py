from collections import deque


class MinStack:

    def __init__(self):
        self.min_stack_highscore = deque() # 'highscore' stack which keeps track of the smallest encountered values in a stack.
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        try:
            if val <= self.min_stack_highscore[-1]:
                self.min_stack_highscore.append(val)
        except IndexError:
            self.min_stack_highscore.append(val)

    def pop(self) -> None:
        pop_val = self.stack.pop()  # Pop the top value of stack
        try:
            if pop_val == self.min_stack_highscore[-1]:
                # if the popped value is equal to the current
                # minimum value, we must pop it from the min_stack
                self.min_stack_highscore.pop()
        except IndexError:
            pass

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack_highscore[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Explanation:
For the basic stack functionality of popping and pushing, we can use the python built in data structure 'deque'. We call
this variable just 'stack', which will hold all of the values that are pushed into it (and also will remove any that are 
popped). However, to keep track of the minimum value in the stack, we need an extra deque. This extra deque is called
'min_stack_highscore'. This min_stack_highscore is a sort of 'highscore' list which keeps track of all the lowest values. At first,
it is empty, but when the first value is pushed in our MinStack object, it will be pushed into both the regular stack and
also the min_stack_highscore stack. Whenever a new value is pushed into MinStack, it will firstly be pushed into the regular
stack, and subsequently be compared to the top value of the min_stack_highscore stack. If the new value is lower than/equal to the
top value of the min_stack_highscore stack, it will also be pushed onto the min_stack_highscore stack. Then, whenever we 
pop a value from the regular stack, we check if the value that is being popped is the current top value in the 
min_stack_highscore stack. If so, we will pop from the min_stack_highscore as well, since we are 'losing' that lowest
value from the regular stack (so it should no longer exist anymore in our MinStack object, meaning we should remove it
from our min_stack_highscore too. Unless there was a duplicate minimum value such as two -100000 values. 
This is accounted for by using 'smaller than/equal to' when checking if a newly
pushed value onto the regular stack should also be pushed onto the min_stack_highscore stack). 
When someone calls the min_value function, we should simply return the top value of the min_stack_highscore stack 
which is O(1) since it is a deque. 
"""