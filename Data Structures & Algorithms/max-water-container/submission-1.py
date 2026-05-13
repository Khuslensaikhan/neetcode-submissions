class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        area = 0
        mostArea = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            mostArea = max(area, mostArea)

            if heights[left] <= heights[right]:
                left += 1
            else: 
                right -= 1
        return mostArea





        