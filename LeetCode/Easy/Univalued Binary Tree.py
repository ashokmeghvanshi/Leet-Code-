# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def checktree(node,l):
            if node==None:
                return None
            checktree(node.left,l)
            l.append(node.val)
            checktree(node.right,l)
            
            return l
            
        l=[]
        t=checktree(root,l)
        if l.count(l[0])==len(l):
            return True
        else:
            return False
