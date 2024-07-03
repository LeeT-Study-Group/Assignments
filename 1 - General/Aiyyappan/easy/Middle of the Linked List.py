# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        c=head
        temp=head
        count=0
        while temp:
            count=count+1
            temp=temp.next
        ind=count//2
        for i in range(ind):
            c=c.next
        return c
    

        
        