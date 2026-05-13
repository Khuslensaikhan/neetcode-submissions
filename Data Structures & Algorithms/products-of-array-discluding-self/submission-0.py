# So products is number * number * number .... = products

# 1. multiplying every numbers in the array and divide it by the current index. 
#     TC = Big O (n)
#     MM = Big O (n)

# 2. we can use prefix and suffix 
# basically we multiply current element with previous elements and save as prefix
# then we go back to left and do the same and save it as a postfix
# result = prefix * postfix 

# input: array = size of 1000; array[i] = max 20
# output: array 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i] 

        postfix = 1 
        for j in range(n-1, -1, -1):
            result[j] *= postfix
            postfix *= nums[j] 

        return result
    