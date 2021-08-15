# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        def height(node):
            if node is None:
                return 0
            else:
                return max(height(node.left),height(node.right))+1
        
        h=height(root)
        
        def avglevel(node,f,level):
            if node is None:
                return
            if level==1:
                f.append(node.val)
                #print(a)
            else:
                avglevel(node.left,f,level-1)
                avglevel(node.right,f,level-1)
        
        
        ans=[]
        for i in range(1,h+1):
            self.a=[]
            avglevel(root,self.a,i)
            s=sum(self.a)
            l=len(self.a)
            #print(s,l)
            ans.append(s/l)
            
        return ans
        
