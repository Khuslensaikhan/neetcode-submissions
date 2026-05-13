class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Input: Numbers of List int and Target int.
        # Output: indices i and j that nums[i] + nums[j] == target and i!=j.
        # Assumptions: Exactly one pair of i and j, return with the small index.

        # Create a hash map to store the value and index of each element in the array.
        hashMap = {}
        # Iterate through the array and compute the complement of the current element, which is target - nums[i].
        for i, n in enumerate(nums):
            hashMap[n] = i

        for i, n in enumerate(nums):
            difference = target - n 
            if difference in hashMap and hashMap[difference] != i:
                return [i, hashMap[difference]]
        return []
        # Check if the complement exists in the hash map.
        # If it does, return the indices of the current element and its complement.
        # If no such pair is found, return an empty array.