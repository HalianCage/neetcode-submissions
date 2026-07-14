# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = [[root.val]]
        tListNum = []
        tListNode = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                tListNode.append(node.left)
                tListNum.append(node.left.val)
            if node.right:
                tListNode.append(node.right)
                tListNum.append(node.right.val)

            if not queue:
                queue.extend(tListNode)
                res.append(tListNum)
                tListNum = []
                tListNode = []

        return res[:len(res)-1]
        