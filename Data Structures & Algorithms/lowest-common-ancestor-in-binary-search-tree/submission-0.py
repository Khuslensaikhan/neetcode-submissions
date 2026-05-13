# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p and q is both > root we go right subtree
        # if p and q is noth < root we go left subtree
        # if p > root and q < root or p < root and q > root we return root
        # if p = root or q = root we return root

        if p.val > root.val and q.val < root.val:
            return root

        if p.val < root.val and q.val > root.val:
            return root

        if p.val == root.val or q.val ==root.val:
            return root

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return None
