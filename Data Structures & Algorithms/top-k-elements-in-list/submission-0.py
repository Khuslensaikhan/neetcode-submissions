
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Input: nums = [1, 2, 2, 3, 3, 3], k = 2
        # Output: [2, 3]
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        array = []
        for num, count in count.items():
            array.append([count, num])
        array.sort()

        result = []
        while len(result) < k:
            result.append(array.pop()[1])

        return result