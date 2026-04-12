# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #will have recursion find, but the recursion is in
        #a while loop, if both of them are less than the root.val
        #do recursive find on the left side
        #if both of them are larger than root value
        #do recursion on right side
        #else one of them is the root than return the root
        while root:
            if p.val<root.val and q.val<root.val:
                root = root.left
            elif p.val>root.val and q.val>root.val:
                root =  root.right
            else:
                return root
            






