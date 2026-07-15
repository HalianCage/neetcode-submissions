# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        sortedList = []

        def treeToList(node):
            
            if node.left:
                treeToList(node.left)
            
            sortedList.append(node.val)

            if node.right:
                treeToList(node.right)

        treeToList(root)

        return sortedList[k-1]
