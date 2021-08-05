# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.ans=1000000
        self.pre=-1
        
        def helper(node):
            
            if node!=None:
                helper(node.right)
                if self.pre!=-1:
                    diff=self.pre-node.val
                    self.ans=min(self.ans,diff)
                self.pre=node.val
                #print(node.val,self.ans,self.pre)
                
                helper(node.left)
            
        helper(root)
        #print(self.ans)
        return self.ans
