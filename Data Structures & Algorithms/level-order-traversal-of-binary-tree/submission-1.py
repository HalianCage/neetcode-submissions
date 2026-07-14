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
        q = deque([root])

        while q:
            
            while q:
                node = q.popleft()

                if node.left:
                    tListNum.append(node.left.val)
                    tListNode.append(node.left)

                if node.right:
                    tListNum.append(node.right.val)
                    tListNode.append(node.right)

            q.extend(tListNode)
            res.append(tListNum)
            tListNode = []
            tListNum = []

        return res[:len(res)-1]