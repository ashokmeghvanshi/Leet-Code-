# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        self.SumEV=0
        
        def SumEvenValue(root,SumEV):
            if root==None:
                return 0
            if root and root.val%2==0:
                
                if root.left!=None:
                    if root.left.left!=None:
                        self.SumEV=self.SumEV+root.left.left.val
                    if root.left.right!=None:
                        self.SumEV=self.SumEV+root.left.right.val
                
                if root.right!=None:
                    if root.right.left!=None:
                        self.SumEV=self.SumEV+root.right.left.val
                    if root.right.right!=None:
                        self.SumEV=self.SumEV+root.right.right.val
            
            if root.left!=None:
                SumEvenValue(root.left,self.SumEV)
            if root.right!=None:
                SumEvenValue(root.right,self.SumEV)
            
            return self.SumEV
        
        return SumEvenValue(root,self.SumEV)
            
