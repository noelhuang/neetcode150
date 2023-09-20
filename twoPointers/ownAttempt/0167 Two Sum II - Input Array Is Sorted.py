from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = None
        for i in range(len(numbers) - 1):
            if numbers[i] == cache:
                continue
            elif numbers[i] > target / 2:
                continue
            cache = numbers[i]
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] > target:
                    break
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]