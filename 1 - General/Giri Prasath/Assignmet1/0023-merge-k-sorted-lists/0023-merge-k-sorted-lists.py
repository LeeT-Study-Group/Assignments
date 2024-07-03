# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        x = []
        for i in range(len(lists)):
            a = lists[i]  
            while a:
                x.append(a.val)
                a = a.next
        x.sort()
        y = ListNode(0)
        i = y
        
        for val in x:
            i.next = ListNode(val)
            i = i.next

        return y.next

        
