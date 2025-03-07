# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol = []

        def postorder(node):
            if node == None:
                return
            postorder(node.left)
            postorder(node.right)
            sol.append(node.val)

        postorder(root)
        return sol
