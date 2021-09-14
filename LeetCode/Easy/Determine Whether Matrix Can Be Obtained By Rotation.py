class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        if mat==target:
            return True
        
        def transpose(mt):
            
            x=[[0 for j in range(len(mt[0]))] for i in range(len(mt))]
            #print(x)
            for i in range(len(mt)):
                for j in range(len(mt[0])):
                    x[i][j]=mt[len(mt)-1-j][i]
            #print(x)
            return x
            
        
        i=0
        while i<4:
            t=transpose(mat)
            if t==target:
                return True
            mat=t
            i=i+1
            
        return False
