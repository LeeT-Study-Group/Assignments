# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def sortBST(node):
            if not node:   
                 return []
            return sortBST(node.left) + [node.val] + sortBST(node.right)
        sorted_list = sortBST(root)
        ans = temp = TreeNode(sorted_list[0])
        for i in range(1, len(sorted_list)):
            temp.right = TreeNode(sorted_list[i])
            temp = temp.right    
        return ans