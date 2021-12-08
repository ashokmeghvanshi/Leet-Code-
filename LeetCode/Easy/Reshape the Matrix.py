class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        r1=len(mat)
        c1=len(mat[0])
        
        if r1*c1!=r*c:
            return mat
        
        #ans=[[0 for i in range(c)]for i in range(r)]
        
        middle=[]
        
        for i in range(r1):
            for j in range(c1):
                middle.append(mat[i][j])
        
        ans=[]
        
        x=0
        y=r
        while y>0:
            ans.append(middle[x:x+c])
            x=x+c
            y=y-1
            
            
        #print(ans,middle)
        
        return ans
