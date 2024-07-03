# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stk = []
        def dfs(root):
            if not root: return
            stk.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)

        for i in range(len(stk)-1):
            stk[i].left = None
            stk[i].right = stk[i+1]
        return root