# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        
        def preorder(node):
            if node:
                if node.left is None and node.right is None:
                    return str(node.val)+''
                if node.right is None:
                    return str(node.val)+'('+preorder(node.left)+')'
                else:
                    return str(node.val)+'('+preorder(node.left)+')'+'('+preorder(node.right)+')'
                
            return ''
        return preorder(t)
                
