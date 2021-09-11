# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def create(array):
            if len(array)==0:
                return None
            
            l=len(array)//2
            
            node=TreeNode(array[l])
            
            node.left=create(array[:l])
            node.right=create(array[l+1:])
            return node
        
        return create(nums)
