# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def trav(node):
            if not node:
                return []
            return trav(node.left) + [node.val] + trav(node.right)

        sorted = trav(root)

        def bst(val):
            if not val:
                return None
            mid = len(val) // 2
            root = TreeNode(val[mid])
            root.left = bst(val[:mid])
            root.right = bst(val[mid + 1:])
            return root

        return bst(sorted)

