# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, leftb, rightb):
            if not node:
                return True
            if not leftb < node.val < rightb:
                return False
            return (helper(node.left, leftb, node.val) and 
                        helper(node.right, node.val, rightb))
        return helper(root, float('-inf'), float('inf'))
