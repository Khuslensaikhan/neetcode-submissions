class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        # nums = [3,4,5,6], target = 7
        for i, num in enumerate(nums):
            x = target - num
            if x in hashMap:
                return [hashMap[x], i]
            hashMap[num] = i
        return []
