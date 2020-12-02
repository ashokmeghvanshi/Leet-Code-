# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue=[]
        queue.append(root)
        
        while len(queue)>0:
            deepsum=0
            currlevelsize=len(queue)
            i=0
            while i < currlevelsize:
                currnode=queue.pop(0)
                deepsum=deepsum+currnode.val
                
                if currnode.left!=None:
                    queue.append(currnode.left)
                if currnode.right!=None:
                    queue.append(currnode.right)
                i=i+1
            
        return deepsum
