class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1 #goal is the last index

        for i in range(n-1, -1, -1):
             maxJumps = nums[i]
             if i + maxJumps >= goal:
                goal = i

        if goal == 0:
            return True
        return False