# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        tList = []
        q = deque([root])

        # Adding all tree elements, including None, into a list with BFS approach
        while q:
            node = q.popleft()

            if not node:
                tList.append(node)
                continue
            
            tList.append(node.val)
            q.append(node.left)
            q.append(node.right)

        
        # converting tList to single string
        string = ""
        for n in tList:
            string += str(n) + "#"

        return string

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split("#")
        nodes = nodes[:-1]
        eleQ = deque(nodes)
        nodeQ = deque()

        def eleToEle(ele):

            nonlocal nodeQ
            
            if ele != "None":
                ele = int(ele)
                node = TreeNode(ele)
                nodeQ.append(node)
            else:
                node = None
            return node

        root = eleToEle(eleQ.popleft())

        while eleQ:
            parent = nodeQ.popleft()

            ele = eleQ.popleft()
            node = eleToEle(ele)

            parent.left = node

            ele = eleQ.popleft()
            node = eleToEle(ele)

            parent.right = node

        return root
            
