# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.findDepth(root)

    
    def findDepth(self, node):
        if node is None:
            return 0
        
    
        leftDepth = self.findDepth(node.left)
        rightDepth = self.findDepth(node.right)

        return 1 + max(leftDepth,rightDepth)
        