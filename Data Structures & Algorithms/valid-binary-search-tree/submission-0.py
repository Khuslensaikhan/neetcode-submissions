# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Binary Tree is Valid when
        #left node is < root we go left and check children
        #right node is > root we go right and check children
        def dfs(node, leftChild, rightChild):
            if not node:
                return True

            if not (leftChild < node.val < rightChild):
                return False

            return dfs(node.left, leftChild, node.val) and dfs(node.right, node.val, rightChild)
    
        return dfs(root, float('-inf'), float('inf'))