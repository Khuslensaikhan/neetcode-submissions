# Input: numbers = [1,2,3,4], target = 3
#                   l r

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1

        while left < right:
            currSum = numbers[left] + numbers[right]
            
            if currSum < target:
                left += 1
            elif currSum > target:
                right-= 1 
            else: 
                return [left+1, right+1]

        return []
                
            