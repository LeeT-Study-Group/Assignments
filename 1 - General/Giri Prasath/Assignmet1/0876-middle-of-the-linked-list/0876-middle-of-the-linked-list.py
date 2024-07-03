# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        new = head
        while new is not None:
            count += 1
            new = new.next
        
        ni = count // 2

        new = head
        for _ in range(ni):
            new = new.next
        
        return new

        