from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        bfs = []
        while queue:
            l = len(queue)
            lvl = []
            for _ in range(l):
                node = queue.popleft()
                if node is not None:
                    lvl.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if lvl:
                bfs.append(lvl)
                    
        return bfs
        