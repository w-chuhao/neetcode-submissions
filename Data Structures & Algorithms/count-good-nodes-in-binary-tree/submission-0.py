# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.value = 0
        self.count = 0

        self.dfs(root,-math.inf)
        return self.count
    

    def dfs(self,node,curr_max):
        if node is None:
            return None

        if node.val >= curr_max:
            self.count += 1
        curr_max = max(curr_max,node.val)

        self.dfs(node.left,curr_max)
        self.dfs(node.right,curr_max)
        


        
        
        