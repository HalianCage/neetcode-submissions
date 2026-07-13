# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return

        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
        
        if self.isSubtree(root.left, subRoot):
            return True
        if self.isSubtree(root.right, subRoot):
            return True

        return False

    def isSameTree(self, p, q) -> bool:
        
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            isEqlL = self.isSameTree(p.left, q.left)
            isEqlR = self.isSameTree(p.right, q.right)

            return isEqlL and isEqlR

        return False
        