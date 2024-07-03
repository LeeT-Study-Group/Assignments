class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1, p2 = head, head
        while p1 is not None and p1.next is not None:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                return True
        return False