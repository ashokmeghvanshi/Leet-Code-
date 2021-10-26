# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        
        def mergetree(node1,node2):
            if node1 is None:
                return node2
            if node2 is None:
                return node1
            node1.val=node1.val+node2.val
            
            node1.left=mergetree(node1.left,node2.left)
            node1.right=mergetree(node1.right,node2.right)
            return node1
        
        return mergetree(root1,root2)
