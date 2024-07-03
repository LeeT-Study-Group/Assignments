/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func reverseKGroup(head *ListNode, k int) *ListNode {
    if k==1{
        return head
    }
    var start,next,tail,prev *ListNode
    var status bool
    for head!=nil{
        head, tail, next, status = conditionedReverse(head,k)
        if start == nil {
            start = head
        }
        if !status{
            prev.Next = reverse(head)
            break
        }
        if prev!=nil{
            prev.Next = head
        }
        head = next
        prev = tail
    }
    return start
}

func reverse(node *ListNode) *ListNode {
    var prev *ListNode
    for node!=nil {
        nxt := node.Next
        node.Next = prev
        prev = node
        node = nxt
    }
    return prev
}

func conditionedReverse(node *ListNode, k int) (head, tail, next *ListNode, status bool) {
    tail = node
    for k>0 && node != nil{
        next = node.Next
        node.Next = head
        head = node
        node = next
        k--
    }
    status = (k==0)
    return
}