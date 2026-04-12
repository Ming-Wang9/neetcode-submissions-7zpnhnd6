# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf') 
        def dfs (root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            l_max =max(left, 0)
            r_max =max(right, 0)
            self.max_sum = max(self.max_sum, root.val+l_max+r_max)
            return root.val+max(l_max, r_max)
        dfs(root)
        return self.max_sum
