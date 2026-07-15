# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        list = [float('-inf'), float('inf')]

        return self.isValid(root, list)
        

    def isValid(self, root:Optional[TreeNode], valRange:list[int]) -> bool:

        if not root:
            return True

        if root.val < valRange[1] and root.val > valRange[0]:
            return self.isValid(root.left, [valRange[0], root.val]) and self.isValid(root.right, [root.val, valRange[1]])
        else:
            return False