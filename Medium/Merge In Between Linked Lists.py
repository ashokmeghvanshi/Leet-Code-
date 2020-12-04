# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        node=list1
        a_index=0
        while a_index<a-1:
            node=node.next
            a_index=a_index+1
        
        node_copy=node
        b_index=0
        while b_index<=b-a+1:
            node_copy=node_copy.next
            b_index=b_index+1
        
        node.next=list2
        count=list2
        while count.next!=None:
            count=count.next
        count.next=node_copy
        
        return list1
        
        
