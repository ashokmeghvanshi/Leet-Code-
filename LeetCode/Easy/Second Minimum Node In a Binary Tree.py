# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.ans=set()
        
        def helper(node):
            if node:
                self.ans.add(node.val)
                helper(node.left)
                helper(node.right)    
                    
                    
        helper(root)
        #print(self.ans)
        self.ans=sorted(self.ans)
        if len(self.ans)<2:
            return -1
        else:
            return self.ans[1]
            
        
        
