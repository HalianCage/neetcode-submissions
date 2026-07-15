# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {}

        for i,n in enumerate(inorder):
            mp[n] = i

        index = 0
        l, r = 0, len(preorder)-1

        def dfs(l, r):

            nonlocal index
            
            if l > r:
                return

            value = preorder[index]
            index += 1
            mid = mp[value]
            node = TreeNode(value)
            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)
            return node

        return dfs(l, r)
