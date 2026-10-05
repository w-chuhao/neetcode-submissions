# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.preOrder(root,p,q)

    def preOrder(self, node, p, q):

        if not node:
            return None

        if p.val < node.val and q.val < node.val:
            return self.preOrder(node.left, p, q)

        if p.val > node.val and q.val > node.val:
            return self.preOrder(node.right, p, q)

        return node
        