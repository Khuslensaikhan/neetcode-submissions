'''
Observations:
1. Input is sorted array in ascending order. 
2. It has been rotated between 1 and n times.
    - Rotating means indexes are moving to the end of an array.
    - nums = [1,2,3,4,5,6] rotate 4 times become [3,4,5,6,1,2]
              0 1 2 3 4 5                         2 3 4 5 0 1
3. Rotating by len(nums) times produces the original array.

Objective: 
(All elements in the rotated sorted array nums are unique)
(Negative number can be in the array)
1. Return the minimum element of this array.
2. Run time should be O (log n)

'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:

            mid = (left + right) // 2 

            if nums[mid] > nums[right]:
                left = mid + 1 
            else: 
                right = mid 

        return nums[left]




