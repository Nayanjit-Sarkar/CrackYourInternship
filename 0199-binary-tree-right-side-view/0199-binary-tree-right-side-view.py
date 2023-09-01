from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        queue = deque()
        lvl,i=[],0
        lvl.append(root.val)
        queue.append(root.right)
        queue.append(root.left)
        while queue:
            i=0
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node:
                    if i == 0:
                        lvl.append(node.val)
                        i = 1
                    queue.append(node.right)
                    queue.append(node.left)
    
        
        return lvl