# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        
        self.help={}
        
        def helper(node):
            if node:
                value=node.val
                if value not in self.help:
                    self.help[value]=0
                else:
                    self.help[value]=self.help[value]+1
                helper(node.left)
                helper(node.right)
                
        helper(root)
        max_freq=max(self.help.values())
        ans=[]
        for i in self.help:
            if self.help[i]==max_freq:
                ans.append(i)
        return ans
            
