# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Instead of scanning index we can use hashmap at inorder:
        inOrderMap = {val: idx for idx, val in enumerate(inorder)} #O(n)
        self.preIdx = 0 #track current root in preorder

        def dfs(left, right):
            if left > right:
                return None
            rootValue = preorder[self.preIdx]
            self.preIdx += 1 

            #creating a BST
            root = TreeNode(rootValue)

            mid = inOrderMap[rootValue] #O(1) lookup instead of scan index

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(inorder) - 1)