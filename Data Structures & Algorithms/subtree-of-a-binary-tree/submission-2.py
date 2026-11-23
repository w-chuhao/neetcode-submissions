# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
                return True

        if not root:
            return False

        # Check if current subtree matches subRoot
        if self.isSameTree(root, subRoot):
            return True

        # Otherwise, check left and right subtrees
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def isSameTree(self, p, q):

        # Both trees are empty
        if not p and not q:
            return True

        # One tree is empty, or values are different
        if not p or not q or p.val != q.val:
            return False

        # Both left and right subtrees must match
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
            


        
        