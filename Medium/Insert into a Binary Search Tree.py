# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root==None:
            return TreeNode(val)
        
        def insertBST(node,val):
            if node is None:
                return TreeNode(val)
            else:
                if node.val<val:
                    node.right=insertBST(node.right,val)
                elif node.val>val:
                    node.left=insertBST(node.left,val)
            return node
                
        insertBST(root,val)
        return root
