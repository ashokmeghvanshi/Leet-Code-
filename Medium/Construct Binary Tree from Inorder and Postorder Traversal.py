# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def Tree_to_INPOST(inorder,postorder):
            
            if len(inorder)==0:
                return 
            new_element=postorder.pop()
            node=TreeNode(new_element)
            element_index=inorder.index(new_element)
            
            node.right=Tree_to_INPOST(inorder[element_index+1:],postorder)
            node.left=Tree_to_INPOST(inorder[:element_index],postorder)
            
            return node
            
        return Tree_to_INPOST(inorder,postorder)
    
