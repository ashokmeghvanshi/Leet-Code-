"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def pre(root,l):
            if root==None:
                return None
            
            l.append(root.val)
            for i in root.children:
                pre(i,l)
                
        l=[]
        pre(root,l)
        return l
