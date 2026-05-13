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
        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]

            










        