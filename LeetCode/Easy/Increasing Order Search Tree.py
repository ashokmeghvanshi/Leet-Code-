# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        self.ans=[]
        
        def helper(node):
            if node:
                helper(node.left)
                self.ans.append(node.val)
                helper(node.right)
            
        helper(root)
        #print(self.ans)
        
        result=new_node=TreeNode(self.ans[0])
        
        #new_node.right=TreeNode
        
        for i in self.ans[1:]:
            new_node.right=TreeNode(i)
            new_node=new_node.right
        return result
