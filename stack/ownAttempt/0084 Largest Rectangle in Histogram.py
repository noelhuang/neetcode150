from collections import deque


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Initialize array of potential answers
        rectangles = []
        unique_heights = set(heights)
        for height in unique_heights:
            filtered_heights = [True if x >= height else False for x in heights]

            max_len = 0
            current_len = 0
            for boolean in filtered_heights:
                if boolean:
                    current_len += 1
                    if current_len > max_len:
                        max_len = current_len
                else:
                    current_len = 0
            rectangles.append(max_len * height)

        return max(rectangles)


"""
"""