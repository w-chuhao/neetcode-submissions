# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.mp = {}
        for i in range(len(inorder)):
            self.mp[inorder[i]] = i

        self.index = 0

        return self.dfs(0,len(preorder)-1,preorder)
        

    def dfs(self,left,right,preorder):

        if left>right:
            return None

        value = preorder[self.index]
        self.index+=1
        root = TreeNode(value)

        curr = self.mp[value]

        root.left = self.dfs(left,curr-1,preorder)
        root.right = self.dfs(curr+1,right,preorder)

        return root


