/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 func build(preorder *[]int, inorder []int) *TreeNode {
    if len(inorder) == 1 {
        *preorder = (*preorder)[1:]
        return &TreeNode{
            Val:inorder[0],
        }
    }
    node := TreeNode{}
    node.Val = (*preorder)[0]
    *preorder = (*preorder)[1:]
    left := []int{}
    right := []int{}
    for idx, x := range inorder {
        if x == node.Val{
            left = inorder[:idx]
            right = inorder[idx+1:]
            break
        }
    }
    if len(left) > 0{
        node.Left = build(preorder, left)
    }
    if len(right) > 0 {
        node.Right = build(preorder, right)
    }
    return &node
}

func buildTree(preorder []int, inorder []int) *TreeNode {
    return build(&preorder, inorder)
}