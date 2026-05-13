# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
My observations:
We are given roots of two binary tree. p and q.
Return True if the trees are same else False

Can we do recursive dfs to traverse through both trees together until 
they finishes traversing and if we caught the different nodes return False 
1. We want to traverse through the both trees at the same time and compare 
2. Return false if nodes doesn't have same children
3. If both nodes are none return True 
4. If only one node is none return False
5. both exist but value differ return False
6. Otherwise check left subtree and right subtree recursively
'''

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False
    
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        






