# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = 0
        self.dfs(root)
        return self.ans

    
    def dfs(self, node):
        if node is None:
            return None

        self.dfs(node.left)
        self.count+=1
        if self.count == k:
            self.ans = node.val
            return None
        self.dfs(node.right)
        

        