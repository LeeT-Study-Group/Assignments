class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head
        
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        current.next = head
        
        k = k % length
        
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        new_tail.next = None
        
        return new_head
