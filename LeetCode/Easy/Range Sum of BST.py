# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def check(node,l,h,ans):
            
            #print(ans,node.val)
            
            if node.val>=l and node.val<=h:
                ans=ans+node.val
                
            if node.left!=None:
                ans=check(node.left,l,h,ans)
            
            if node.right!=None:
                ans=check(node.right,l,h,ans)
            
            return ans
        
        return check(root,low,high,0)
        
        
