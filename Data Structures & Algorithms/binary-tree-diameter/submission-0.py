# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0
        self.post_order(root)
        return self.max_d


    
    def post_order(self, node):

        if node is None:
            return 0

        left_d = self.post_order(node.left)
        right_d = self.post_order(node.right)

        self.max_d = max(self.max_d, left_d+right_d)

        return 1 + max(left_d, right_d)

        