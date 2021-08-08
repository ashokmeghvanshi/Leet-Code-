# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        self.ans=[]
        def helper(node):
            #print(node.val)
            if node:
                if node.left is None and node.right is None:
                    self.ans.append(node.val)
                    return
            
                helper(node.left)
                helper(node.right)
            
        helper(root1)
        helper(root2)
        #print(self.ans)
        
        if len(self.ans)%2!=0:
            return False
        else:
            half=len(self.ans)//2
            if self.ans[:half]==self.ans[half:]:
                return True
            else:
                return False
