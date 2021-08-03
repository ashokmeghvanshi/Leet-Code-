# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        self.ans=0
        def check(node,s):
            
            if node.left==None and node.right==None:
                s=s+str(node.val)
                self.ans=self.ans+int(s,2)
                return
            
            s=s+str(node.val)
            
            if node.left!=None:
                check(node.left,s)
            
            if node.right!=None:
                check(node.right,s)
                
        check(root,'')
        return self.ans
