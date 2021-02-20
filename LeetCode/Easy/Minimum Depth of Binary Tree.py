# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        def MinDepth(root):
            if root==None:
                return 0
            if root.left==None and root.right==None:
                return 1
            if root.left==None:
                return MinDepth(root.right)+1
            if root.right==None:
                return MinDepth(root.left)+1
            
            return min(MinDepth(root.left),MinDepth(root.right))+1
            
            
        return MinDepth(root)
            
