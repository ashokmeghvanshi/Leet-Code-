# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.ans=[]
        
        def helper(node,s):
            if node:
                if node.left!=None or node.right!=None:
                    s=s+str(node.val)+'->'
                if node.left==None and node.right==None:
                    s=s+str(node.val)
                    self.ans.append(s)
                    return
                helper(node.left,s)
                helper(node.right,s)
                
                
        helper(root,'')
        #print(self.ans)
        
        return self.ans
