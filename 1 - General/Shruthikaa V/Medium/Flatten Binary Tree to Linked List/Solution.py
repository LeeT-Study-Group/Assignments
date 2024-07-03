# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def flatten_helper(node):
            nonlocal prev
            if not node:
                return

            right_subtree = node.right
            node.left = None
            flatten_helper(node.left)
            flatten_helper(right_subtree)
            node.right = node.left
            prev.right = node
            prev = node
        
        prev = TreeNode()
        
        flatten_helper(root)
