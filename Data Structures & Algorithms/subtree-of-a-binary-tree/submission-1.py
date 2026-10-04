# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root,subRoot)

        
    
    def dfs(self, node, target):
        if not node:
            return False
        
        if node.val == target.val and self.isSameTree(node, target):
            return True
        
        return(self.dfs(node.left,target) or
            self.dfs(node.right, target))

    
    def isSameTree(self, node, target):

        if not node and not target:
            return True
        
        if not node:
            return False
        
        if not target:
            return False
        
        if node.val != target.val:
            return False
        
        return (self.isSameTree(node.left,target.left) and self.isSameTree(node.right,target.right))

        


        
        