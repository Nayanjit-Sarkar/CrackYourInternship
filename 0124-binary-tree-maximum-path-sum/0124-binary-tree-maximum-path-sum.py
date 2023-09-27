# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
            if root is None:
                return
            res = [root.val]
            def dfs(root):
                if root is None:
                    return 0
                leftS = max( dfs(root.left), 0)
                rightS = max(dfs(root.right), 0)
                res[0] = max(res[0], root.val+leftS+rightS)
                return root.val+ max(leftS, rightS) 
            res[0] = max(dfs(root), res[0])
            return res[0]