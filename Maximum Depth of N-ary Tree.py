"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def helper(node):
            if node is None:
                return 0
            else:
                maxdepth=0
                for i in node.children:
                    maxdepth=max(maxdepth,helper(i))
                return maxdepth+1
            
        return helper(root)
