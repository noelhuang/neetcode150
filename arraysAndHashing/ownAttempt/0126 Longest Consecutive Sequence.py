from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Iterate over input array
        # Put all values into hashset
        hash_set = set(nums)
        max_length = 0
        # Pop random value from hashset
        while len(hash_set) > 0:
            curr_length = 0
            initial_val = next(iter(hash_set))
            curr_val = initial_val
            # Lookup upper neighbour, and continue popping in that direction (U*O(1)), if found increment
            while curr_val in hash_set:
                hash_set.discard(curr_val)
                curr_val += 1
                curr_length += 1

            # reset current value to initially popped value -1 to check lower neighbours
            curr_val = initial_val - 1
            # Lookup lower neighbour, and continue popping in that direction (L*O(1)), if found increment
            while curr_val in hash_set:
                hash_set.discard(curr_val)
                curr_val -= 1
                curr_length += 1
            # Update max length if current length is larger
            if curr_length > max_length:
                max_length = curr_length

        return max_length
