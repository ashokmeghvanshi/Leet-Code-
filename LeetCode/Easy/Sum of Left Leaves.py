# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum1=0
        def sumleftleaves(root):
            if root==None :
                return 
            if root.left and root.left.left is None and root.left.right is None:
                self.sum1+=root.left.val
            sumleftleaves(root.left)
            sumleftleaves(root.right)
        sumleftleaves(root)
        return self.sum1
