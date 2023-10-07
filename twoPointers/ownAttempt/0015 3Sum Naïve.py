from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        my_set = set()
        num_len = len(nums)

        my_map = {}
        for i in range(num_len):
            if nums[i] in my_map:
                my_map[nums[i]].add(i)
            else:
                my_map[nums[i]] = {i}

        for i in range(0, num_len):
            for j in range(i + 1, num_len):
                # does the counterpart to i + j exist? if so, make a triplet and add it to the set
                # if not, continue
                counterpart = 0 - (nums[i] + nums[j])
                if counterpart in my_map:
                    # check if counterpart list has a value which is not i or j by discarding i and j from the set
                    for index in my_map[counterpart]:
                        if index != i and index != j:
                            triplet = [nums[i], nums[j], counterpart]
                            triplet.sort()
                            my_set.add(tuple(triplet))
        return list(my_set)
