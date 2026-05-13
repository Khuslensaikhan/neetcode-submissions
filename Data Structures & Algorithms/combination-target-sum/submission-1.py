class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
    
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return 

            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res


        


# def backtrack(path, choice_list):
#     if termination_condition_met:
#         result.add(path)
#         return

#     for choice in choice_list:
#         make_choice
#         backtrack(path, choice_list)
#         undo_choice