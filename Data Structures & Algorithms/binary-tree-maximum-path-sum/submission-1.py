# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Observations:
1. how to get the path? 
2. What is not path in BST?
3. how to count the sum?
4. what to not count?

example: Input: root = [-15,10,20,null,null,15,5,-5]
we have a pathSum = 0 to count the sum

at each node:
1. what is the best path that passes through this node:
    = node.val + best_left + best_right

and what you return to parents:
    node.val + max(best_left, best_right)
'''

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float('-inf')
        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            self.result = max(self.result, left + right + node.val)
            
            return node.val + max(left, right)
        dfs(root)  
        return self.result






        