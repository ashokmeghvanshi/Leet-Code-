# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result1=[]
        result2=[]
        def getelement(node,result):
            if node==None:
                return 
            getelement(node.left,result)
            result.append(node.val)
            getelement(node.right,result)
            
        getelement(root1,result1)
        getelement(root2,result2)
        result=sorted(result2+result1)
        return result
