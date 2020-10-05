# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(node1):
            if node1==None:
                return 0
            lh1=height(node1.left)
            rh1=height(node1.right)
            return 1+max(lh1,rh1) 
        
        def path(node):
            if node==None:
                return 0
            lh=height(node.left)
            rh=height(node.right)
            
            ld=path(node.left)
            rd=path(node.right)
            return max(lh+rh,max(ld,rd))
        return path(root)
