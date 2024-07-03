/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode increasingBST(TreeNode root) {
        List<Integer> vals = new ArrayList<>();
        inorder(root, vals);
        TreeNode newRoot = new TreeNode(0); 
        TreeNode curr = newRoot;
        for(int val : vals) {
            curr.right = new TreeNode(val);
            curr = curr.right;
        }
        return newRoot.right;
    }
    
    private void inorder(TreeNode node, List<Integer> vals) {
        if(node==null) return;
        inorder(node.left, vals);
        vals.add(node.val);
        inorder(node.right, vals);
    }
}