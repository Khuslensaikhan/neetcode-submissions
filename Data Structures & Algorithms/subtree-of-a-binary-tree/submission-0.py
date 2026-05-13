# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
So I need two objecive: 
1. Walk through every node of the main tree using DFS
2. At each node, check if the subtree starting here is exactly same as subRoot

Algorithm: 
1. If subRoot is empty return True. (Empty tree is always a subtree)
2. if root is empty return False. (no subtree can be in nothing)
3. At the current root node:
    if sameTree(root, subRoot) is True, return True.
4. Recursively check:
5. return True if either side returns True.
'''

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


    def sameTree(self, q, p):
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
        return True




        