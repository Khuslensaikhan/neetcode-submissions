class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0 
        maxSum = float('-inf')
        n = len(nums)

        for i in range(n):
            currentSum += nums[i]
            if currentSum > maxSum:
                maxSum = max(currentSum, maxSum)
            if currentSum < 0:
                currentSum = 0
        return maxSum

