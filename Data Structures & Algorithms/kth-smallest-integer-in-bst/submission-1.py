# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # keep decreasing k while doing dfs on left, if k is still 
        # larger than 0, do dfs on right
        res =[]
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res[k-1]