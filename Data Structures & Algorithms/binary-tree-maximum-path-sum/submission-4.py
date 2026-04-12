# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = float('-inf')
        def dfs (root):
            if not root:
                return 0
            left_gain = max(dfs(root.left), 0)
            right_gain = max(dfs(root.right), 0)
            cur_path = root.val + left_gain+right_gain
            self.maxsum = max(self.maxsum, cur_path)
            return root.val + max(left_gain, right_gain)
        dfs(root)
        return self.maxsum
            

