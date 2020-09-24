"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def post(root,l):
            if root==None:
                return None
            
            for i in root.children:
                post(i,l)
            l.append(root.val)
                
        l=[]
        post(root,l)
        return l
