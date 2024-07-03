# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        r = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(r)
        dummy = itr = ListNode()
        while l and r:
            if l.val < r.val:
                nxt = l.next
                l.next = None
                itr.next = l
                itr = itr.next
                l = nxt
            else:
                nxt = r.next
                r.next = None
                itr.next = r
                itr = itr.next
                r = nxt
        if l:
            itr.next = l
        if r:
            itr.next = r
        return dummy.next