# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(node,t):
            
            if node ==None:
                return
            
            if node!=None:
                if node.left==None and node.right==None:
                    t.append([node.val,0])
                
                elif node.left!=None and node.right!=None:
                    t.append([node.val,2])
                
                elif node.left!=None:
                    t.append([node.val,-1])
                
                elif node.right!=None:
                    t.append([node.val,1])
                    
                check(node.left,t)
                check(node.right,t)
            
            return t
        
        arr1=[]
        arr2=[]
        check(root,arr1)
        check(subRoot,arr2)
        
        #print(arr1,arr2)
        
        l=len(arr2)
        if arr1==arr2:
            return True
        for i in range(len(arr1)-l+1):
            #print(arr1[i:i+l],arr2)
            if arr1[i:i+l]==arr2:
                return True
        
        return False
