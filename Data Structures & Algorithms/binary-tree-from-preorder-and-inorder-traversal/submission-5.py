# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder: root|left|right
        #inorder: left|root|right
        if not preorder or not inorder:
            return None
        rootval = preorder[0]
        root = TreeNode(rootval)
        rootidx = inorder.index(rootval)
        root.left = self.buildTree(preorder[1:rootidx+1], inorder[:rootidx+1])
        root.right = self.buildTree(preorder[rootidx+1:], inorder[rootidx+1:])
        return root