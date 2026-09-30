# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        height = self.getHeight(root)

        return self.isBalanced

    def getHeight(self,node):

        if node is None:
            return 0

        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)

        if abs(right_height - left_height) > 1:
            self.isBalanced = False

        return 1 + max(left_height,right_height)


        
        
        