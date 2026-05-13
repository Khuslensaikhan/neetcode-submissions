class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Algorithm
        # Build a frequency map that counts how many times each number appears.
        count = {}
        # Create a list of groups freq, where freq[i] will store all numbers that appear exactly i times.
        freq = [[] for i in range(len(nums) + 1)]
        # For each number and its frequency in the map, add the number to freq[frequency].
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        # Initialize an empty result list.
        res = []
        # Loop from the largest possible frequency down to 1:
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        # For each number in freq[i], add it to the result list.
        # Once the result contains k numbers, return it.