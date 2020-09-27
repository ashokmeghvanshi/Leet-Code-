# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def helper(node,t):
            if node==None:
                return None
            helper(node.left,t)
            t.append(node.val)
            helper(node.right,t)
            return t
        t=[]
        check=helper(root,t)
        for i in range(len(check)-1):
            for j in range(i+1,len(check)):
                if check[i]+check[j]==k:
                    return True
        return False
            
