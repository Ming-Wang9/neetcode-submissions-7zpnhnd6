class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def isSame(n1, n2):
            if not n1 and not n2:
                return True
            if n1 and n2 and n1.val == n2.val:
                return isSame(n1.left, n2.left) and isSame(n1.right, n2.right)
            return False

        # main logic: check current node, or recurse left/right
        return (
            isSame(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
