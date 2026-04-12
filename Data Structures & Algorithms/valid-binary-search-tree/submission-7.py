# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #not only locally work
        #need to have left and right boundry
        def dfs(node, leftlow, righthigh):
            if not node:
                return True
            if not leftlow<node.val<righthigh:
                return False
            return dfs(node.left, leftlow, node.val) and dfs(node.right, node.val,righthigh)
        return dfs(root, float('-inf'), float('inf'))








