# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        p1 = p2 = head
        count = 0
        while p1:
            count += 1
            p1 = p1.next
        p1 = head
        k = k % count
        if k == 0 :
            return head
        while k>=0:
            k -=1 
            p2 = p2.next
        while p2:
            p1 = p1.next
            p2 = p2.next
        new_head = p1.next
        p1.next = None
        itr = new_head
        while itr and itr.next:
            itr = itr.next
        if itr:
            itr.next = head
        return new_head