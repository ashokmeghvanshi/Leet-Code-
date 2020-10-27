# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s=''
        node=head
        while node!=None:
            s=s+str(node.val)
            node=node.next
        
        t=int(s,2)
        return t
