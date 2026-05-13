# So basically we are trying to find the biggest area can be made using this array.
# height[i] is the height of any container
# and the i shoulde be the bar number. 

# which means: height[i] * i = area

# question is which height I should take and which bar I should take
# i should have 2 bars to make container so we can say that we get lower bar number as height
# and i should take second bar index - first bar index = breadth
# breadth * height = area
# return area 

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1 
        maxArea = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            maxArea = max(area, maxArea)
            if heights[left] < heights[right]:
                left += 1 
            else:
                right -= 1
        return maxArea
