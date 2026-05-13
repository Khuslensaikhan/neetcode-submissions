
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        sequence = 0

        for i in hashSet:
            if i - 1  not in hashSet: 
                longest = 1
                while (i + longest) in hashSet:
                    longest += 1
                sequence = max(sequence, longest)

        return sequence