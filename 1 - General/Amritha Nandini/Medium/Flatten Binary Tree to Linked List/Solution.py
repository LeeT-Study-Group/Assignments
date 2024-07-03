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
        if not root:
            return None
        left = root.left
        right = root.right
        
        self.flatten(left)
        self.flatten(right)

        if left:
            left_rightmost = left
            while left_rightmost.right:
                left_rightmost = left_rightmost.right

            left_rightmost.right = root.right
            root.right = left
            root.left = None