# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Let's implement recursive DFS 
        if not root:
            return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)
'''

'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Let's implement iterative DFS
        if not root:
            return 0
        stack = [[root, 1]]
        res = 0

        while stack: 
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        result = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            result += 1
        return result










