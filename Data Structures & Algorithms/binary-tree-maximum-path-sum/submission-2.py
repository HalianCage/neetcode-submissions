# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        pathSum = root.val

        def maxPath(root):

            nonlocal pathSum

            if not root:
                return 0

            leftTotal = maxPath(root.left)
            rightTotal = maxPath(root.right)

            subTreeTotal = root.val + leftTotal + rightTotal
            currTotal = root.val + max(leftTotal, rightTotal)

            pathSum = max(subTreeTotal, pathSum)

            return currTotal if currTotal > 0 else 0

        maxPath(root)

        return pathSum


        