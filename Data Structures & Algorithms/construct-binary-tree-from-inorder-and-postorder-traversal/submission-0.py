# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        mp = {n:i for i,n in enumerate(inorder)}

        idx = len(postorder)-1
        
        def dfs(l, r):

            if l > r:
                return None

            nonlocal idx

            val = postorder[idx]
            idx -= 1
            node = TreeNode(val)
            mid = mp[val]
            node.right = dfs(mid+1, r)
            node.left = dfs(l, mid-1)
            return node

        return dfs(0, len(inorder)-1)

            