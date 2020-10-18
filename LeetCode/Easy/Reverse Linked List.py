# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current=head
        prev=None
        
        while current!=None:
            t=current.next
            current.next=prev
            prev=current
            current=t
        head=prev
        return head
