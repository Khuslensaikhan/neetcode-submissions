class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Input: Numbers of List int and Target int.
        # Output: indices i and j that nums[i] + nums[j] == target and i!=j.
        # Assumptions: Exactly one pair of i and j, return with the small index.
        solution = []
        for i in range(len(nums)): 
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]