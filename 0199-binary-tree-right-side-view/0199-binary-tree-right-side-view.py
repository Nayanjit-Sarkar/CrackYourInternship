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
        lvl,i={},0
        lvl[i] = root.val
        queue.append(root.right)
        queue.append(root.left)
        while queue:
            i+=1
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node:
                    if i not in lvl:
                        lvl[i] = node.val
                    queue.append(node.right)
                    queue.append(node.left)
        res = []
        for i in lvl:
            res.append(lvl[i])
        return res